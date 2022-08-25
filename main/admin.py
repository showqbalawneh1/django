from django.contrib import admin
from .models import tutorial ,tutorialCategory ,tutorialSeries
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class tutorialAdmin(admin.ModelAdmin):
    fieldsets = [ 
        ("title date" , {"fields": ["tutorialTitle","tutorialPublished"]}),
        ("content" , {"fields": ["tutorialContent"]}),
        ("URL", {'fields': ["tutorialSlug"]}),
        ("Series", {'fields': ["seriesTutorial"]}),
        
    ]
    formfield_overrides={
        models.TextField:{'widget' : TinyMCE()}
    }
    
''' fields=["tutorialTitle",
            "tutorialPublished",
            "tutorialContent"
            ]'''
       
    
admin.site.register(tutorial ,tutorialAdmin )
admin.site.register(tutorialSeries)
admin.site.register(tutorialCategory)