from django.shortcuts import render
from PrimerMVT import Familia


def familia(self):
    familia= Familia(nombre="Vanesa", fechadenac="1979-01-28", edad="43")
    familia.save()
    