from socket import fromshare
from django import forms



class Reservaform (forms.Form):
    nombre= forms.CharField(max_length = 30)
    fecha= forms.DateField()
    comensales= forms.IntegerField()


class Clienteform (forms.Form):
    nombre= forms.CharField(max_length = 30)
    direccion= forms.CharField(max_length = 30)
    edad= forms.IntegerField


class Barform (forms.Form):
    nombre= forms.CharField(max_length = 30)
    direccion= forms.CharField(max_length = 30)
    especialidad= forms.CharField(max_length = 300)
