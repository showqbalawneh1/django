from django.contrib import admin
from .models import tutorial 
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class tutorialAdmin(admin.ModelAdmin):
    fieldsets = [ 
        ("title date" , {"fields": ["tutorialTitle","tutorialPublished"]}),
        ("content" , {"fields": ["tutorialContent"]})
    ]
    formfield_overrides={
        models.TextField:{'widget' : TinyMCE()}
    }
    
''' fields=["tutorialTitle",
            "tutorialPublished",
            "tutorialContent"
            ]'''
       
    
admin.site.register(tutorial ,tutorialAdmin )
