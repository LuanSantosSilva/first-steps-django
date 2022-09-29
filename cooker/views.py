from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'cooker/pages/home.html', context={'name':'Luan'})
