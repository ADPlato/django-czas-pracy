from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WorkingReportForm
from .models import Employee
# Create your views here.

def index_view(request):
    return render(request, 'index.html')

def employees_view(request):
    #employee_list = Employee.objects.all()
    #render(request, )
    pass

def managers_view(request):
    pass

def time_view(request):
    form = WorkingReportForm(request.POST or None)

@login_required
def add_worktime_report(request):
    form = WorkingReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(index_view)
    return render(request, 'work_time_form.html', {'form':form})


def project_view(request):
    pass

def teams_view(request):
    pass
