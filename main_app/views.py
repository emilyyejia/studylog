from django.shortcuts import render
from .models import Problem

def home(request):
    return  render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def problem_index(request):
    problems =  Problem.objects.all()
    return render(request,'problems/index.html', {'problems': problems})

def problem_detail(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    return render(request, 'problems/detail.html', {'problem': problem})