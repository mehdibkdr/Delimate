from django.shortcuts import render, redirect 
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm, CreateDelivererForm, UpdateDelivererForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record, Deliverer
from django.contrib import messages
from django.db.models import F

# - Homepage 

def home(request):

    return render(request, 'webapp/index.html')

# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)

# - Login a user

def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")

    context = {'form':form}

    return render(request, 'webapp/login.html', context=context)

# - User logout

def user_logout(request):

    auth.logout(request)

    return redirect("login")

# - Dashboard

@login_required(login_url='login')
def dashboard(request):

    my_records = Record.objects.all().order_by('-creation_date')
    on_going_tasks = Record.objects.filter(status='on-going')
    completed_tasks = Record.objects.filter(status='completed')

    context = { 'on_going_tasks': on_going_tasks,
                'completed_tasks': completed_tasks,
                'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)

@login_required(login_url='login')

def ongoing(request):
    on_going_tasks = Record.objects.filter(status='on-going')
    context = {'on_going_tasks': on_going_tasks}
    return render(request, 'webapp/ongoing.html', context)

def completed(request):
    completed_tasks = Record.objects.filter(status='completed')
    context = {'completed_tasks': completed_tasks}
    return render(request, 'webapp/completed.html', context)

# - Create Task

def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-task.html', context=context)

# - Update record 

@login_required(login_url='login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/update-task.html', context=context)

# - View record

@login_required(login_url='login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-task.html', context=context)

# - Delete record

@login_required(login_url='login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")

# - Deliverers dashboard

@login_required(login_url='login')
def deliverers_dashboard(request):

    my_deliverers = Deliverer.objects.all().order_by('id')

    context = {'deliverers': my_deliverers}

    return render(request, 'webapp/deliverers-dashboard.html', context=context)

@login_required(login_url='login')

# - Create deliverer

def create_deliverer(request):

    form = CreateDelivererForm()

    if request.method == "POST":

        form = CreateDelivererForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("deliverers_dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-deliverer.html', context=context)

# - Update deliverer 

@login_required(login_url='login')
def update_deliverer(request, pk):

    deliverer = Deliverer.objects.get(id=pk)

    form = UpdateDelivererForm(instance=deliverer)

    if request.method == 'POST':

        form = UpdateDelivererForm(request.POST, instance=deliverer)

        if form.is_valid():

            form.save()

            messages.success(request, "Your deliverer was updated!")

            return redirect("deliverers_dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/update-deliverer.html', context=context)

# - View deliverer

@login_required(login_url='login')
def view_deliverer(request, pk):

    all_deliverers = Deliverer.objects.get(id=pk)

    context = {'deliverer':all_deliverers}

    return render(request, 'webapp/view-deliverer.html', context=context)

# - Delete deliverer

@login_required(login_url='login')
def delete_deliverer(request, pk):

    deliverer = Deliverer.objects.get(id=pk)

    deliverer.delete()

    messages.success(request, "Your deliverer was deleted!")

    return redirect('deliverers_dashboard')