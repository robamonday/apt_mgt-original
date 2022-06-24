from django.db import models

# Create your models here.

class Unit(models.Model):
	DOWN = 'DOWN'
	VACANT = 'VACANT'
	OCCUPIED = 'OCCUPIED'
	UNIT_STATUS_CHOICES = [
		(DOWN, 'Down'), 
		(VACANT, 'Vacant'), 
		(OCCUPIED, 'Occupied')
		]
	unit_number = models.CharField(max_length=15, blank=False)
	unit_type = models.CharField(max_length=15, blank=False, default="Unknown")
	sf = models.IntegerField(default=0)
	market_rent = models.DecimalField(max_digits=5, decimal_places=0, blank=False)
	unit_status = models.CharField(max_length=15, choices=UNIT_STATUS_CHOICES, default=VACANT)

	def __str__(self):
		return self.unit_number

	# What other methods should go here?

class Lease(models.Model):
	contact = models.CharField(max_length=40, blank=False)
	lease_rent = models.DecimalField(max_digits=5, decimal_places=0, blank=False)
	start_date = models.DateField()
	end_date = models.DateField()
	unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.contact

	# What other methods should go here?



class LedgerEntry(models.Model):
	pass	



# class State(models.Model):
#   stateName = models.CharField(max_length=50, verbose_name="State Name")
#   stateAbbreviation = models.CharField(max_length=3, verbose_name="State Abbreviation")
#   def __str__(self):
#     return '{}'.format(self.stateName)
#   def get_absolute_url(self):
#     return "/tourist_attractions/"

# class Attraction(models.Model):
#   homeState = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="Home State")
#   attractionName = models.CharField(max_length=200, verbose_name="Attraction Name")
#   def __str__(self):
#     return '{}'.format(self.attractionName)
#   def get_absolute_url(self):
#     return "/tourist_attractions/"