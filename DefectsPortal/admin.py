from django.contrib import admin
from DefectsPortal.models import Defects_screen_shots, DefectsList

# Register your models here.
class DefectListAdmin(admin.ModelAdmin):
    list_display = ['defect_name','assigned_to','defect_status']

admin.site.register(DefectsList,DefectListAdmin)
admin.site.register(Defects_screen_shots)