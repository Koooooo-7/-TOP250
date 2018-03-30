from django.conf.urls import  url
from  . import  views
urlpatterns = [
    url(r'^home/$',views.home,name="home")   #功能，页面分配
]
