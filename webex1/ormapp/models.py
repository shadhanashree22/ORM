from django.db import models
from django.contrib import admin
class Book(models.Model):
  serialno=models.IntegerField(primary_key=True);
  booklanguage=models.CharField(max_length=20);
  bookauthor=models.CharField(max_length=20);
  editionno=models.IntegerField();
  duedate=models.DateField();

class BookAdmin(admin.ModelAdmin):
   list_display=("serialno","booklanguage","bookauthor","editionno","duedate")


