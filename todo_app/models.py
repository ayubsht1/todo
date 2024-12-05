from django.db import models

# Create your models here.
class Todo(models.Model): #inherit models.Model
    title = models.CharField(max_length=200)#varchae,char
    decription = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.title
    
