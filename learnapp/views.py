from django.shortcuts import render,redirect
from DefectsPortal.models import DefectsList
from learnapp.forms import UserProfileForm,UserForm,UserEditForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserProfileForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()

            profile = form2.save(commit=False)
            profile.user = user  # connecting default user model and custom model
            profile.save()
            registered = True
    else:
        form1 = UserForm
        form2 = UserProfileForm
    context = {
        'form1':form1,
        'form2':form2,
        'registered':registered
    }
    return render(request,'registeration.html',context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # authentication step
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("please check your creds..!")

    return render(request,'login.html')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    total_defects = DefectsList.objects.all()
    
    total_defects_assigned = 0
    total_defects_completed = 0
    total_defects_pending = 0
    total_primary_money = 0
    total_secondary_money = 0
    total_amount = 0

    for defect in total_defects:
        if request.user.username == defect.assigned_to:
            total_defects_assigned += 1
            if defect.defect_status == 'COMPLETED':
                total_defects_completed += 1
                
                # Ensure defect_type is checked properly
                if defect.defect_type.upper() == "PRIMARY":
                    total_primary_money += 8000
                elif defect.defect_type.upper() == "SECONDARY":
                    total_secondary_money += 4000

            elif defect.defect_status == 'NOT COMPLETED':
                total_defects_pending += 1

    # Compute total amount correctly
    total_amount = total_primary_money + total_secondary_money

    context = {
        'total_defects_assigned': total_defects_assigned,
        'total_defects_completed': total_defects_completed,
        'total_defects_pending': total_defects_pending,
        'total_primary_money': total_primary_money,
        'total_secondary_money': total_secondary_money,
        'total_amount': total_amount  # Ensure this is included
    }
    
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def userEdit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserEditForm(instance=request.user)
    return render(request,'edit.html',{'form':form})


