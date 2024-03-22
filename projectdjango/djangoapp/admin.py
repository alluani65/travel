from django.contrib import admin

# Register your models here.
from . models import Testimonical,Ceo,Manager,Background

admin.site.register(Testimonical)
admin.site.register(Ceo)
admin.site.register(Manager)
admin.site.register(Background)