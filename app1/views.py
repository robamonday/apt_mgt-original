from django.shortcuts import render, get_object_or_404
# from .models import State, Attraction
# from .forms import StateCreateForm, AttractionCreateForm
# from django.views.generic.edit import CreateView

def home(request):
  context = {"key" : "value"}
  return render(request, 'app1/base.html', context)

# def details(request, statename):
#   attractions = Attraction.objects.all()
#   context = {"attractions" : attractions, "statename" : statename.replace("-", " ")}
#   return render(request, 'tourist_attractions/details.html', context)

# class StateCreate(CreateView):
#   model = State
#   form_class = StateCreateForm
#   template_name = "tourist_attractions/state_create_form.html"

# class AttractionCreate(CreateView):
#   model = Attraction
#   form_class = AttractionCreateForm
#   template_name = "tourist_attractions/attraction_create_form.html"
