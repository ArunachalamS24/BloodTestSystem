from django.contrib import admin
from .models import *

# Register your models here.

class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ['name','gender','age','email','phnNo','password','address']
    list_filter = ['gender']
    search_fields = ['name']

admin.site.register(UserRegister,UserRegisterAdmin)

class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ['name','email','feedback','date']

admin.site.register(UserFeedback,UserFeedbackAdmin)


