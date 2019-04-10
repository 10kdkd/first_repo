from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    price = models.CharField(max_length = 20)
    book_grade_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    grade = models.CharField(max_length = 5, choices = book_grade_choices, default = '3')
    
    def __str__(self):
        return self.title