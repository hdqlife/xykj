from . import views
from django.conf.urls import url


urlpatterns = [
   url(r'board/',views.board),
   url(r'msg/',views.msg),
]