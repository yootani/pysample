from django.conf.urls import include, url
from . import views

# ApplicationName
app_name = 'doc'
# ここで、views.pyに記述したメソッド名を指定することで、ルーティングの設定が可能になる。
urlpatterns = [
	url(r'^$', views.doc_list),
]
