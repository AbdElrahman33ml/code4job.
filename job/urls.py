from django.urls import path,include
from . import views 
from . import views 


app_name='job'
urlpatterns = [
    path('', views.job_list,name='job_list'),
    path('add_job', views.add_job,name='add_job'),
    path('<str:slug>', views.job_details,name='job_details')
]