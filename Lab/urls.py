from django.urls import path
from .views import *

urlpatterns = [
    path('register/',LabRegistration, name = 'LabRegister'),
    path('login/', LabLogin, name = 'LabLogin'),
    path('', LabIndex, name = 'LabIndex'),
    path('logout/',LabLogout, name = 'LabLogout' ),
    path('labprofile/',LabProfile,name = 'LabProfile'),
    path('appointment/',PatientAppointment, name = 'PatientAppointment'),
    path('editappointment/<int:id>', EditAppointment, name = 'EditAppointment'),
    path('approvedAppointment/', approvedAppointment, name = 'approvedAppointment'),
    path('takeTest/<int:id>', takeTest, name = 'takeTest'),
    path('viewCat/', viewCat, name = 'viewCat'),
    path('addCat/',addCat, name = 'addCat'),
    path('editCat/<int:id>', editCat, name = 'editCat'),
    path('deleteCat/<int:id>', deleteCat, name = 'deleteCat'),
    path('viewFeedback/', viewFeedback, name = 'viewFeedback'),
    path('showFeedback/<int:id>', showFeedback, name = 'showFeedback'),
    path('viewTestLab/<int:id>', viewTestLab, name = 'viewTestLab'),
    path('deleteTest/<int:id>', deleteTest, name = 'deleteTest')

]