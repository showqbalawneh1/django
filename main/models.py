from django.db import models

# Create your models here.
class tutorial (models.Model):
    tutorialTitle = models.CharField(max_length=200)#Required. The maximum length (in characters) of the field.
    tutorialContent =models.TextField("")
    tutorialPublished = models.DateTimeField("date published ")
    
    #we can make various overwrite 
    def __str__(self):
        return self.tutorialTitle
    