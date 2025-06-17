from django.urls import path, re_path

from menu import views


urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.show_all_menu, name='menu'),
    re_path(r'^menu/(?P<path>.+)/$', views.show_path, name='path'),
]