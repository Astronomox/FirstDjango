from django.forms import Modelform

from .models import UserDetails

class UserForm(Modelform):
    class Meta:
        model=UserDetails