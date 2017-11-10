import uuid
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import RegisterForm
from .models import Activate
from myapp.backends import EmailOrUsernameModelBackend


def index(request):
    """ / でアクセス　トップ画面 """

    context = {
        'user': request.user,
    }
    return render(request, 'main/index.html', context)


def activation(request, key):
    """ /activation/:アクティベーションキー　でアクセス　本登録画面 """

    # keyを使ってactivateモデルを取得
    activate = get_object_or_404(Activate, key=key)

    # activateモデルに紐づいたユーザオブジェクトを取得
    user = activate.user

    # is_activeをTrue(アカウントの有効化)にし、保存
    user.is_active = True
    user.save()

    # view側でログインさせる際は、login()関数が必要
    user.backend = EmailOrUsernameModelBackend
    login(request, user)

    context = {
        'user': user,
    }
    return render(request, 'main/profile.html', context)


@login_required
def profile(request):
    """ /profileでアクセス、プロフィール画面 """

    context = {
        'user': request.user,
    }
    return render(request, 'main/profile.html', context)


def regist(request):
    """ /regist でアクセス　ユーザ登録画面に遷移する """

    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'main/regist.html', context)


@require_POST
def regist_save(request):
    """ /regist_saveでアクセス ユーザ仮登録処理 """

    form = RegisterForm(request.POST)
    if form.is_valid():

        # 仮登録処理 is_activeをFalseに
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # activateモデルの作成と保存 userモデルを紐付ける
        # uuidを使ったランダムな文字列作成
        activate_key = create_key()
        activate_instance = Activate(user=user, key=activate_key)
        activate_instance.save()

        # メール本文の「本登録はこちら！ http://...」のURLを作成する
        base_url = "/".join(request.build_absolute_uri().split("/")[:3])
        activation_url = "{0}/activation/{1}".format(base_url, activate_key)

        user.email_user("題名", "本登録は以下のURLから！\\n" + activation_url)
        return redirect('main:index')

    context = {
        'form': form,
    }
    return render(request, 'main/regist.html', context)


def create_key():
    """ ランダムな文字列を生成する """

    key = uuid.uuid4().hex
    return key
