from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import json

from .models import Proveedor
from vnt.forms import ProveedorForm

class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'vnt/proveedor_list.html'
    context_object_name = 'obj'
    permission_required='vnt.view_proveedor'


class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = 'vnt/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('vnt:proveedor_list')
    login_url = 'basescerbeus:login'
   


    def post(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().post(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = 'vnt/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('vnt:proveedor_list')
    login_url = 'basescerbeus:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)


def proveedorInactivar(request, id):
    template_name = 'vnt/inactivar_prv.html'
    contexto = {}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe' + str(id))

    if request.method == 'POST':
        contexto = {'obj':prv}

    if request.method == 'GET':
        prv.estado = False
        prv.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')

    return render(request, template_name, contexto)


# Create your views here.
