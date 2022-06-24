from django.shortcuts import render, get_object_or_404
from .models import Unit, Lease, LedgerEntry
# from .forms import StateCreateForm, AttractionCreateForm
# from django.views.generic.edit import ListView, CreateView

unit1 = Unit(unit_number="A-1", unit_type="1x1", sf=1000, market_rent=2000, unit_status="Occupied")
unit2 = Unit(unit_number="A-2", unit_type="1x1", sf=1000, market_rent=2000, unit_status="Vacant")
unit3 = Unit(unit_number="A-3", unit_type="1x1", sf=1000, market_rent=2000, unit_status="Vacant")
unit4 = Unit(unit_number="A-4", unit_type="1x1", sf=1000, market_rent=2000, unit_status="Vacant")
unit5 = Unit(unit_number="A-5", unit_type="1x1", sf=1000, market_rent=2000, unit_status="Vacant")
unit6 = Unit(unit_number="A-6", unit_type="1x1", sf=1000, market_rent=2000, unit_status="Vacant")
unit7 = Unit(unit_number="A-7", unit_type="1x1", sf=1000, market_rent=2000, unit_status="Vacant")
unit8 = Unit(unit_number="A-8", unit_type="1x1", sf=1000, market_rent=2000, unit_status="Vacant")
unit9 = Unit(unit_number="A-9", unit_type="1x1", sf=1000, market_rent=2000, unit_status="Down")
unit1.save()
unit2.save()
unit3.save()
unit4.save()
unit5.save()
unit6.save()
unit7.save()
unit8.save()
unit9.save()

def home(request):
  context = {"key" : "value"}
  return render(request, 'app1/home.html', context)

def units(request):
  units = Unit.objects.all()
  context = { "units" : units }
  return render(request, 'app1/units.html', context)








# template for views
# 
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
