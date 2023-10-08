from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'nombre':'Néstor',
                                        'apellido':'Marlier'})

def pag404(request):
    return render(request,'404.html')