from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
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

class ProblemAdd(CreateView):
    model = Problem
    fields = '__all__'

class ProblemUpdate(UpdateView):
    model = Problem
    fields = ['description']

class ProblemDelete(DeleteView):
    model = Problem
    success_url = '/problems/'