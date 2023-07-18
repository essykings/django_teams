from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_created']

    
class Task(models.Model):
    TODO="TO DO"
    COMPLETED='COMPLETED'
    INPROGRESS='IN-PROGRESS'
    STATUS_CHOICES = [
        (TODO, 'TO DO'),
        (COMPLETED, 'COMPLETED'),
        (INPROGRESS, 'IN-PROGRESS'),
       

    ]
    title = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True)
    project = models.ForeignKey(Project,null=True,blank=True, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, null=True,blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,null=True,blank=True,default= TODO)
    

    def __str__(self):
        return self.title
 
