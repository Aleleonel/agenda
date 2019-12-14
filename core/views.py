from django.shortcuts import render
from .models import Evento


def lista_eventos(request):
    eventos = Evento.objects.all()
    dados = {'eventos': eventos}

    return render(request, 'agenda.html', dados)
