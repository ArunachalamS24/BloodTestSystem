from django.urls import path
from .views import *

urlpatterns = [
    path('',Index, name = 'index'),
    path('register/',Register, name = 'register'),
    path('login/',Login, name = 'login'),
    path('logout/',Logout, name ='logout'),
    path('UserProfile/',UserProfile, name = 'UserProfile'), 
    path('bookAppointment/',bookAppointment, name = 'bookAppointment'),
    path('appointmentStatus/', appointmentStatus, name = 'appointmentStatus'),
    path('deleteAppointment/<int:id>', deleteAppointment, name = 'deleteAppointment'),
    path('Feedback/', Feedback , name = 'Feedback'),
    path('viewTest/<int:id>',viewTest, name = 'viewTest')   
]