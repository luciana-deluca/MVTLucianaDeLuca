from django.shortcuts import render
from PrimerMVT import Familia
from django.template import loader
from django.http import HttpResponse

def familia(self):
    familia= Familia(nombre="Vanesa", fechadenac="1979-01-28", edad="43")
    familia.save()
    temp = loader.get_template("templatemvt.html")
    documento = temp.render(familia)
    return HttpResponse(documento)
    