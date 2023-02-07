from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def mostrar (req):
    
    return render(req,"calc.html")

def calcular (req):
    try:
        if req.method=="post":
            n1=eval(req.post.get("num1"))
            n2=eval(req.post.get("num2"))
            op=eval(req.post.get("operation"))
            if op=="+":
                c=n1+n2
                messages.warning(req, 'Tu perfil ha sido actualizado.')
            elif op=="-":
                c=n1-n2
            elif op=="*":
                c=n1*n2
            elif op=="/":
                c=n1/n2            
    except:
        c="Operacion no valida"

    return render(req,"calc.html")

