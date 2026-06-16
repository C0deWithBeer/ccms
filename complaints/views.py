from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Complaint
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

###
###  COMMON
###

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form  = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {"form": form})


###
###  COMMON
###


    context = {
        'username': 'Peer Mohamed',
        'role': 'normal'
    }
    return render(request, 'home.html', context)

def logout_user(request):
    logout(request)
    return redirect('/')

def home(request):
    if request.user.is_authenticated:
        has_logged_in = True
        role = 'admin' if request.user.is_staff else 'user'
        username = request.user.username
    else:
        has_logged_in = False
        role = None
        username = 'Anonyms'

    context = {
        'has_logged_in': has_logged_in,
        'role': role,
        'username': username
    }

    return render(request, 'home.html', context)

###
###  User Specific
###

@login_required
def create_complaint(request):
    if request.method == 'POST':
        title: str = request.POST['title']
        description: str = request.POST['description']
        
        Complaint.objects.create(
            title=title,
            description=description,
            status="OPEN",
            user=request.user
        )

        return redirect("/")
    
    else:
        return render(request, 'create_complaint.html')

@login_required
def view_own_complaints(request):
    complaints = Complaint.objects.filter(
        user=request.user
    )

    paginator = Paginator(complaints, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'title': 'View Own Complaints'}
    return render(request, 'complaint_list.html', context)


###
###  Admin Specific
###
@login_required
def view_all_complaints(request):
    complaints = Complaint.objects.all()
    query = request.GET.get('q')

    if query:
        complaints = complaints.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    
    ## Pagination
    paginator = Paginator(complaints, 5) # 10 complaints per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj, 
        'title': "View All Complaints",
        'query': query
    }

    return render(request, 'complaint_list.html', context)

@login_required
def update_complaint_status(request, complaint_id):
    ## restricting normal users from accessing it
    if not request.user.is_staff:
        return HttpResponse("Access Denied")
    
    ## get the complaint object from DB
    complaint = Complaint.objects.get(id=complaint_id)

    if not complaint:
        return HttpResponseNotFound("complaint not found")

    ## checking is this post request
    if request.method == 'POST':
        new_status = request.POST['status']
        
        complaint.status = new_status

        complaint.save()

        return redirect(f'/manage/complaints/{complaint.id}')
    
    context = {
        'complaint': complaint
    }
    
    return render(request, 'update_complaint.html', context)