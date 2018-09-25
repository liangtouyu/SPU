from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.csrf import csrf_exempt

from db.base_view import BaseVerifyView
from sp_user.forms import RegisterForm, LoginForm
from sp_user.helper import verify_login_required
from sp_user.models import User


class RegisterView(View):
    def get(self, request):
        # 使用form渲染html
        form = RegisterForm()
        return render(request, 'sp_user/reg.html', {'form': form})

    def post(self, request):
        # 1.接收数据

        # 2.处理数据
        form = RegisterForm(request.POST)
        # 3.响应
        if form.is_valid():
            form.save()
            # 注册成功,跳转登录页面
            return redirect(reverse('sp_user:login'))

        # 注册失败
        return render(request, 'sp_user/reg.html', {'form': form})


# 登陆

class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'sp_user/login.html', {'form': login_form})

    def post(self, request):
        # 接收处理数据
        login_form = LoginForm(request.POST)
        # 响应
        if login_form.is_valid():
            # 验证成功,保存登录标识到session
            user = login_form.cleaned_data.get('user')
            request.session['ID'] = user.pk
            request.session['phone'] = user.phone
            # 设置有效期,关闭浏览器就结束
            request.session.set_expiry(0)

            return redirect(reverse('sp_user:center'))
        # 验证失败
        return render(request, 'sp_user/login.html', {'form': login_form})


class CenterView(View):
    def get(self, request):
        phone = request.session.get('phone')
        context = {
            'phone': phone
        }
        return render(request, 'sp_user/center.html', context)

    def post(self, request):
        pass


class InfoView(BaseVerifyView):
    # 个人资料功能
    def get(self, request):
        # 验证用户是否登录
        user_id = request.session.get("ID")
        # 查询当前用户的所有信息
        user = User.objects.filter(pk=user_id).first()

        context = {
            "user": user
        }
        return render(request, "sp_user/info.html", context)

    def post(self, request):
        # 1. 接收数据
        user_id = request.session.get("ID")
        data = request.POST
        file = request.FILES['head']
        # 2. 处理数据
        # 更新用户的头像
        user = User.objects.get(pk=user_id)
        user.head = file
        user.save()
        # 3. 响应
        return redirect(reverse("sp_user:center"))

        # 单独使用一个视图函数处理图片的上传

    # 验证登录装饰器  放在 公共base里,所有需要验证的页面都需要这个
    # @method_decorator(verify_login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request,*args, **kwargs)


# 登录验证装饰器的使用 函数形式
@csrf_exempt  # 移除令牌限制
def upload_head(request):
    if request.method == "POST":
        # 获取用户的id
        user_id = request.session.get("ID")
        # 获取用户对象
        user = User.objects.get(pk=user_id)
        # 保存图片
        user.head = request.FILES['file']  # 通过键获取对应的文件
        user.save()
        return JsonResponse({"error": 0})
    else:
        return JsonResponse({"error": 1})


@verify_login_required
def info(request):
    return render(request, "sp_user/info.html")
