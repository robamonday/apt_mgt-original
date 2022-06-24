from django.contrib import admin

# Register your models here.
# This 'admin.py' file pertains to the admin interface

from .models import Unit, Lease, LedgerEntry
 
admin.site.register(Unit)
admin.site.register(Lease)
admin.site.register(LedgerEntry)