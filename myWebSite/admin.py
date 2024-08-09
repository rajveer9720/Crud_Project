from django.contrib import admin
from .models import AddStudent

@admin.register(AddStudent)
class AddStudentAdmin(admin.ModelAdmin):
    list_display =('id','name','email','password')

# Register your models here.
