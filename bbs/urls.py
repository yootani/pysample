from django.conf.urls import url
from .views import BbsView

urlpatterns = [
    url(r'^$', BbsView, name='bbs'),
]
