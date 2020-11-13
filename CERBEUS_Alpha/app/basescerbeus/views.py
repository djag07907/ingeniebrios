from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic


class SinPrivilegios(PermissionRequiredMixin):
    login_url: 'basescerbeus:login'
    raise_exception = False
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):
        self.login_url = 'basescerbeus:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'basescerbeus/home.html'
    login_url = 'basescerbeus:login'


class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = 'basescerbeus:login'
    template_name = 'basescerbeus/sin_privilegios.html'
