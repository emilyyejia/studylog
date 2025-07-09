from django.contrib import admin
from .models import Problem, Translation, Tag

admin.site.register(Problem)
admin.site.register(Translation)
admin.site.register(Tag)
