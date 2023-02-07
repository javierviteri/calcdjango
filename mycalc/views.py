from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def mostrar (req):
    
    return render(req,"calc.html")

def calcular (req):
    c=''
    try:
        if req.method=="POST":
            n1=eval(req.POST.get('num1'))
            n2=eval(req.POST.get('num2'))
            op=req.POST.get('operation')
            print(n1)
            print(n2)
            print(op)
            if op=="+":
                c=n1+n2
            elif op=="-":
                c=n1-n2
            elif op=="*":
                c=n1*n2
            elif op=="/":
                c=n1/n2            
    except:
        c="Operacion no valida"
    print(c)
    return render(req,"calc.html",{'c':c})

