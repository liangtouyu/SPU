from django import forms
from django.core import validators
from sp_user.helper import set_password
from sp_user.models import User


# 注册表单
class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 验证手机号码格式是否正确
        self.fields['phone'].validators.append(validators.RegexValidator(r'^1[3-9]\d{9}$', "手机号码格式错误!"))
        # 密码 在form中要求 6-16 个
        self.fields['password'].validators.append(validators.MinLengthValidator(6))
        self.fields['password'].validators.append(validators.MaxLengthValidator(16))

    class Meta:
        model = User
        # 注册只验证手机和密码
        fields = ['phone', 'password']
        # 错误信息提示
        error_messages = {
            'password': {
                'min_length': "密码长度至少6个字符!",
                'max_length': "密码长度不能大于16个字符!",
                'required': "请填写密码!",
            },
            "phone": {
                "required": "手机号码必须填写!",
            }
        }
        # form字段样式设置
        widgets = {
            "phone": forms.TextInput(attrs={'class': 'login-name', 'placeholder': '请输入手机号'}),
            "password": forms.PasswordInput(attrs={'class': 'login-password', 'placeholder': '请输入密码'}),
        }

    # 检测用户手机是否已经被注册
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        rs = User.objects.filter(phone=phone).exists()
        if rs:
            raise forms.ValidationError("该手机号码已经被注册!")
        return phone

    # 综合校验
    def clean(self):
        # 获取所有清洗后的数据
        data = super(RegisterForm, self).clean()

        pwd1 = data.get('password')
        pwd2 = data.get('repassword')
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise forms.ValidationError({'repassword': '两次密码输入不一致!'})
        else:
            # 取密码
            if pwd1:
                # 如果密码不为空 进行加密
                data['password'] = set_password(pwd1)
        return data


# 登陆表单
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        # 只验证用户手机和密码
        fields = ['phone', 'password']
        # 错误信息
        error_messages = {
            'phone': {
                "required": "手机号码必填!",
            },
            "password": {
                "required": "请填写密码!",
                "min_length": "密码不得少于6个字符!",
                "max_length": "密码不得大于16个字符!",
            }
        }

        # 添加前端样式
        widgets = {
            "phone": forms.TextInput(attrs={'class': 'login-name', 'placeholder': '请输入手机号'}),
            "password": forms.PasswordInput(attrs={'class': 'login-password', 'placeholder': '请输入密码'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # 验证手机号码是否正确
        phone = cleaned_data.get('phone')
        password = cleaned_data.get('password')

        # 通过手机号码查询数据,再验证密码,没有直接报错
        user = User.objects.filter(phone=phone).first()

        if user is None:
            raise forms.ValidationError({'phone': '该手机没有注册'})
        else:
            # 验证密码
            password_in_db = user.password  # 加密了

            password = set_password(password)
            if password_in_db != password:
                raise forms.ValidationError({'password': '密码错误'})
            else:
                cleaned_data['user']=user
                return cleaned_data
