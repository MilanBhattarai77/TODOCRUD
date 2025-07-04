from django.contrib import admin
from .models import models


# Register your models here.
from .models import Customer
admin.site.register(Customer)

from .models import Task
admin.site.register(Task)
