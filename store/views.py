from django.shortcuts import render

def home(request):
    return render(request, 'home.html') #line of code to load the template file

def productPage(request):
    return render(request, 'product.html')
   
# Create your views here.
