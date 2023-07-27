from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('base/',views.Base, name='base'),
    path('result/',views.Result, name='result'),
    path('',views.home, name='home'),
    
 
    
] 

urlpatterns += staticfiles_urlpatterns()
