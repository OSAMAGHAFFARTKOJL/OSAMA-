from django.urls import path
from helloworldapp import views
from django.contrib import admin
from django.views.generic import TemplateView



urlpatterns = [
   path('admin/' , admin.site.urls),
   path('', views.hello , name='hello'),
   #path('process-data', views.process_data, name='process_data'),
  

]
