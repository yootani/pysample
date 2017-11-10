============================================================
 Python3 (Django) Start up Project
============================================================

　■　環境

	VM			: Hyper-V
	OS			: Linux Ubuntu 14.04
	言語		: Python 2.7.6
	FrameWork	: Django 1.8.0 final
				: Bootstrap 3.3.7 (Cyborg theme)
	Package		: Django-bootstrap-form 3.3


	another tools
			: pip 9.0.1
			: tree
			: vim
			: xsel

------------------------------------------------------------


 ０．Bootstrapの導入
	①　pipコマンドでインストール
		> sudo pip install django-bootstrap-form

	②　確認
		> pip freeze -l

	③ プロジェクトにBootstrapを追加
		path [ProjectName]/settings.py

		INSTALLED_APPSに以下1行を追加
		[settings.py]
		'bootstrapform',


------------------------------------------------------------

 １．プロジェクトの作成

	①　ワークスペースを作成する
		> mkdir workspace

	②  Djangoプロジェクトを作成する
		> django-admin startproject [ProjectName] .

		* 末尾のドットは、カレンドディレクトリに作成することを指す

	③　タイムゾーンの設定
		> vim /[ProjectName]/settings.py

		1/3/10行目の修正
		[settings.py]
		1 :LANGUAGE_CODE = 'ja'
		2 :
        3 :TIME_ZONE = 'Asia/Tokyo'
		4 :
        5 :USE_I18N = True
		6 :
        7 :USE_L10N = True
		8 :
        10:USE_TZ = False

	④　DBのマイグレーション（標準のSQLite）
		> python3 manage.py migrate

	⑤　サーバーの起動（確認）
		> python3 manage.py runserver



 ２．アプリケーションの作成

	①　アプリケーションの作成
		> python3 manage.py startapp [ApplicationName]


 ３．テーブルの作成

	①　modelに定義を記述　
		> vim /[ProjectName]/[ApplicationName]/models.py

		* 詳細はWeb及びsample_appを確認

	②　modelを有効にする
		> vim /[ProjectName]/settings.py
		* INSTALLEDにmodelに追加したものを記述する

	③　作成したmodelのマイグレーションファイルを作成する
		> python3 manage.py makemigrations [ModelName]

	④　マイグレーションの実行
		> python3 manage.py migrate [MigrationName]


 ３．テーブルの確認

	①　modelをadminに追加する
		> vim /[ApplicationName]/admin.py

		* 詳細はWeb及びsample_appを参照
			(Admin上で編集可能に。importに追加する)

	②　管理者の作成
		> python3 manage.py createsuperuser

	③　ブラウザでテーブルを確認する
		> http://127.0.0.1:8000/admin/



 ４．Templateの編集

	①　Templateファイルを格納するディレクトリを作成する
		path: /[ApplicationName]/

		> mkdir templates
		> mkdir ./templates/[ApplicationName]

			* [ApplicationName]は別名に変更しても可能か？

	②　Templateファイルを作成する
		> touch [TemplateName].html


	③　Viewファイルを変更する
		> vim [ApplicationName]/views.p
			*データをTemplateファイルに送る場合は、Viewで取得し、
			 renderのパラメータとして取得したオブジェクトを渡す。


 ４．ルーティングの設定

	① 　アプリケーションのurls.pyを作成する
		> cp ./myapp/urls.py ./doc/urls.py

	②　urls.pyを編集する
		> vim ./[ApplicationName]/urls.py
			* 対象のアプリケーションのviews.pyに記述した
			 メソッド名を記述する。

		[urls.py]
		1 :from django.conf.urls impot url
		2 :from . import views
		3 :
		4 :urlpatterns = [
		5 :   url(r'^$', views.doc_list),
		6 :]

	③　２で作成したurls.pyをmyappにincludeする
		> vim ./myapp/urls.py

		[urls.py]
		1 :from django.conf.urls import include, url
		2 :from django.contrib import admin
		3 :
		4 :urlpatterns = [
		5 :   url(r'^admin/', include(admin.site.urls)),
		6 :   url(r'', include('doc.urls')),
		7 :]



