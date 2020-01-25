from django.db import models
from django.contrib.postgres.fields import ArrayField

P_CHOICE = (
    (2,'high'),
    (1,'middle'),
    (0,'low'),
)

# COLORS = (
#     ('#f44336', 'red'),
#     ('#e91e63', 'pink'),
#     ('#2196f3', 'blue'),
# )

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    schedule1 = models.CharField(max_length=30, default="No Schedule")
    schedule2 = models.CharField(max_length=30, null="No Schedule")
    color = models.CharField(max_length=7 ,null=True)
    
    def __str__(self):
        return self.name
    

class Exam(models.Model):
    date = models.DateTimeField()
    grade = models.FloatField(default=0)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    typeOf = models.CharField(max_length=7, default="Parcial")

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400, null=True)
    priority = models.CharField(choices=P_CHOICE, max_length=10)
    completed = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    

