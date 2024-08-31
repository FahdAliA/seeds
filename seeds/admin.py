from django.contrib import admin

# Register your models here.
from .models import Events,Startups,GovernBdy,About

admin.site.register(Events)
admin.site.register(Startups)
admin.site.register(GovernBdy)
admin.site.register(About)