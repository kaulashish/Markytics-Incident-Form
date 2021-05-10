from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import IncidentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.
class Home(View):
    def get(self, request):
        all_incidents = Incident.objects.all()
        context = {"incidents": all_incidents}
        return render(request, "index.html", context)


class Login(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")


class Register(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)


class IncidentView(LoginRequiredMixin, View):
    def get(self, request):
        form = IncidentForm()
        context = {"form": form}
        return render(request, "incident_view.html", context)

    def post(self, request):
        # ? VERY IMPORTANT: This is a feature, not a bug.
        # If you want a list of values for a key, use this!
        # using the get method will return the last value in list.
        # print(request.POST.getlist("sub_incident_type"))
        form = IncidentForm(request.POST)
        form.instance.reported_by = request.user
        for i in request.POST.getlist("sub_incident_type"):
            if i == "1":
                form.instance.type_env = True
            if i == "2":
                form.instance.type_inju = True
            if i == "3":
                form.instance.type_property = True
            if i == "4":
                form.instance.type_vehicle = True
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return redirect("home")