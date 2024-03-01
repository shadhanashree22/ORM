# Ex02 Django ORM Web Application
## Date: 1.3.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](<Screenshot 2024-03-01 091312-1.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
admin.py

from django.contrib import admin
from .models import Book,BookAdmin
admin.site.register(Book,BookAdmin)

models.py

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


```


## OUTPUT

![alt text](<Screenshot 2024-03-01 084702-1.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
