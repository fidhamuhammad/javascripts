from django.shortcuts import render

# Create your views here.

def  add(request):
    return render(request,'javascript/add.html')

def  elements(request):
    return render(request,'javascript/elements.html')    

def  largest(request):
    return render(request,'javascript/largest.html')  

def  secondlargest(request):
    return render(request,'javascript/secondlargest.html')     

def  search(request):
    return render(request,'javascript/search.html')           