from django.contrib import admin

from Lab.models import *

# Register your models here.

class LabRegisterAdmin(admin.ModelAdmin):
    list_display = ['LabEmail','LabPassword','LabName','DocName','LabAddress','LabPhone','LabCertificate',]
    search_fields = ['LabName']
    
admin.site.register(LabRegister,LabRegisterAdmin)

admin.site.register(Name_category)
admin.site.register(Test_category)
admin.site.register(Appointment)

admin.site.site_header = 'Lab Administration'                    # default: "Django Administration"
admin.site.index_title = 'Laboratory Diagnosis System'           # default: "Site administration"
admin.site.site_title = 'laboratory diagnosis system' 
