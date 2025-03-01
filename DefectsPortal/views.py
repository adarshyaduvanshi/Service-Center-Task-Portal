from django.shortcuts import render, redirect
from DefectsPortal.models import DefectsList
from django.contrib.auth.decorators import login_required
from DefectsPortal.forms import Defect_Edit_form, add_defect_form
from django.core.paginator import Paginator

@login_required(login_url='login')
def alldefects(request):
    defects = DefectsList.objects.all()
    defect_count = defects.count()  # Get the total count of defects
    paginator = Paginator(defects,4)
    page = request.GET.get('pg')
    defects = paginator.get_page(page)
    return render(request, 'defects/alldefects.html',{'defects':defects,'defect_count': defect_count})

@login_required(login_url='login')
def Defects_description(request,id=0):
    defect = DefectsList.objects.get(id=id)
    return render(request,'defects/description.html',{'defect':defect})

@login_required(login_url='login')
def add_defect(request):
    form = add_defect_form()
    if request.method == 'POST':
        form = add_defect_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('defects')
    return render(request,'defects/add_defects.html',{'form':form})

@login_required(login_url='login')
def update_defects(request,id=0):
    form = Defect_Edit_form(instance=DefectsList.objects.get(id=id))
    if request.method == 'POST':
        form = Defect_Edit_form(request.POST,instance=DefectsList.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('defects')
    return render(request,"defects/edit_defects.html",{'form':form})

@login_required(login_url='login')
def delete_defects(request,id=0):
    defects = DefectsList.objects.get(id=id)
    defects.delete()
    return redirect('defects')




