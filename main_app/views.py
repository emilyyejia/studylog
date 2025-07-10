from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Problem, Tag
from .forms import TranslationForm

def home(request):
    return  render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def problem_index(request):
    problems =  Problem.objects.all()
    return render(request,'problems/index.html', {'problems': problems})

def problem_detail(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    tag_problem_has = problem.tags.all().values_list('id')
    tags = Tag.objects.exclude(id__in=tag_problem_has)
    translation_form = TranslationForm()
    return render(request, 'problems/detail.html', {
        'problem': problem, 'translation_form': translation_form, 'tags':tags
    })

def add_translation(request, problem_id):
    form = TranslationForm(request.POST)
    if form.is_valid():
        new_translation = form.save(commit = False)
        new_translation.problem_id = problem_id
        new_translation.save()
    return redirect('problem_detail', problem_id= problem_id)


class ProblemAdd(CreateView):
    model = Problem
    fields = ['category', 'grade', 'description']

class ProblemUpdate(UpdateView):
    model = Problem
    fields = ['description']

class ProblemDelete(DeleteView):
    model = Problem
    success_url = '/problems/'

class TagCreate(CreateView):
    model = Tag
    fields = '__all__'

class TagList(ListView):
    model = Tag

class TagDetail(DetailView):
    model = Tag

class TagUpdate(UpdateView):
    model = Tag
    fields = ['name', 'color']

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags/'

def associate_tag(request, problem_id, tag_id):
    problem = Problem.objects.get(id=problem_id)
    problem.tags.add(tag_id)
    return redirect('problem_detail', problem_id=problem_id)

def remove_tag(request, problem_id, tag_id):
    problem = Problem.objects.get(id=problem_id)
    problem.tags.remove(tag_id)
    return redirect('problem_detail', problem_id=problem_id)