from django.conf.urls import url
from action import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^login$',views.login),
    url(r'^register$', views.register),
    url(r'^getClass/teacher$', views.getTeacherClass),
    url(r'^addClass$', views.addClass),
    url(r'^updateClass$', views.updateClass),
    url(r'^getTree$',views.getTree),
    url(r'^addTree$', views.addTree),
    url(r'^updateTree$', views.updateTree),
    url(r'^chooseClass$', views.chooseClass),
    url(r'^getClass/student', views.getTeacherClass),
    url(r'^getChooseStudent', views.getChooseStudent),
]