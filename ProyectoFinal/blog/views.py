from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import Reservaform, Clienteform, Barform

def mostrar_inicio(request):
    return render (request, "template/inicio.html")


def procesar_formulario_reserva(request):
    mi_formulario = Reservaform
    contexto = {"formulario": mi_formulario}
    return render (request, "template/formulario-reserva.html", context=contexto)


def procesar_formulario_cliente(request):
    mi_formulario = Clienteform
    contexto = {"formulario": mi_formulario}
    return render (request, "template/formulario-cliente.html", context=contexto)


def procesar_formulario_bar(request):
    mi_formulario = Barform
    contexto = {"formulario": mi_formulario}
    return render (request, "template/formulario-bar.html", context=contexto)

