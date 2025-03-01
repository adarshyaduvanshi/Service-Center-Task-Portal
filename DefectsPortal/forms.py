from django import forms
from DefectsPortal.models import DefectsList 

class add_defect_form(forms.ModelForm):
    class Meta:
        model = DefectsList 
        fields = "__all__" 

class Defect_Edit_form(forms.ModelForm):
    defect_id = forms.CharField(max_length=100,disabled=True)
    defect_type = forms.CharField(disabled=True)
    class Meta:
        model = DefectsList
        fields = "__all__"