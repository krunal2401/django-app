from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmpForm, StudentForm
import csv
from reportlab.pdfgen import canvas  
from .models import Student
# Create your views here.


def getfile(request):
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)
    students = Student.objects.all()  
    for student in students:
        writer.writerow([student.first_name, student.last_name])  
    return response      

def getpdf(request):
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint.")  
    p.showPage()  
    p.save()  
    return response  