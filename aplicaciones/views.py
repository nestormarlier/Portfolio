from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'nombre':'Néstor',
                                        'apellido':'Marlier'})