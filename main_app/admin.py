from django.contrib import admin
from .models import Horse, FarrierAppt, Care

# Register your models here.
admin.site.register(Horse)
admin.site.register(FarrierAppt)
admin.site.register(Care)