from django.db import models
from django.urls import reverse

class Problem(models.Model):
    category = models.CharField(max_length=100)
    grade = models.IntegerField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.category} ({self.grade})'
    def get_absolute_url(self):
        return reverse('problem_detail', kwargs={'problem_id': self.id})