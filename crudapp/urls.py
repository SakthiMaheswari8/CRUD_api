from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addemployee',views.addemployee,name='addemployee'),
    path('employeeget',views.employeeget,name='employeeget'),
    path('employeeget/<int:pk>',views.employeeget,name='employeeget'),
    path('employeeupdates',views.employeeupdates,name='employeeupdates'),
    path('employeeupdates/<int:pk>',views.employeeupdates,name='employeeupdates'),
    path('employeedelete',views.employeedelete,name='employeedelete'),
    path('employeedelete/<int:pk>',views.employeedelete,name='employeedelete'),
]