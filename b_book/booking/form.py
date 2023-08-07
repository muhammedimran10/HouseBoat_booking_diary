
from booking.models import Boat,Trip
from django.forms import ModelForm

class BoatCreationForm(ModelForm):

    class Meta:
        model=Boat
        exclude=['own_by']