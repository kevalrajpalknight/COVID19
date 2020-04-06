from django.contrib import admin
from django.urls import path, re_path, include
from . import views
app_name = 'case'

urlpatterns = [
	re_path(r'^$',views.CaseList.as_view(), name = 'all'),
	re_path(r'^new/',views.CreateCase.as_view(), name = 'create'),
]