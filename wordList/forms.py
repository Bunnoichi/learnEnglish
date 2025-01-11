from django.forms import ModelForm
from .models import Card

class CardForm(ModelForm):
   class Meta:
      model = Card
      fields = ['word', 'meaning', 'note', 'count_appear', 'count_incorrect']