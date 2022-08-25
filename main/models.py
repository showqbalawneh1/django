from django.db import models
from datetime import datetime
# Create your models here.
class tutorialCategory(models.Model):

    categoryTutorial = models.CharField(max_length=200)
    categorySummary = models.CharField(max_length=200)
    categorySlug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.categoryTutorial
    
    
class tutorialSeries(models.Model):
    seriesTutorial = models.CharField(max_length=200)
    categoryTutorial = models.ForeignKey(tutorialCategory,default=None, on_delete=models.SET_DEFAULT)
    seriesSummary = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Series"
    def __str__(self):
        return self.seriesTutorial
    
    
class tutorial (models.Model):
    tutorialTitle = models.CharField(max_length=200)#Required. The maximum length (in characters) of the field.
    tutorialContent = models.TextField("tutorialContent")
    tutorialPublished = models.DateTimeField("date published",default=datetime.now())
    seriesTutorial = models.ForeignKey(tutorialSeries, default=None, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorialSlug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.tutorialTitle
    