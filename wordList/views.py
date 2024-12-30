from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Card
from .forms import CardForm

class IndexView(View):
   def get(self, request):
      return render(request, "wordList/index.html")
   
class CardCreateView(View):
   def get(self, request):
      form = CardForm()
      return render(request, "wordList/card_form.html", {"form": form})
   
   def post(self, request):
      form = CardForm(request.POST)
      if form.is_valid():
         form.save()
         return render(request, "wordList/card_form.html", {"form": form})
      return render(request, "wordList/card_form.html", {"form": form})

class CardListView(View):
   def get(self, request):
      card_list = Card.objects.all()
      return render(request, "wordList/card_list.html", {"card_list": card_list})
   
class CardUpdateView(View):
   def get(self, request, id):
      card = get_object_or_404(Card, id=id)
      form = CardForm(instance=card)
      return render(request,"wordList/card_update.html", {"form": form})
   
   def post(self, request, id):
      card = get_object_or_404(Card, id=id)
      form = CardForm(request.POST, request.FILES, instance=card)
      if "post" in request.POST:
         if form.is_valid():
            form.save()
            return redirect("wordList:index")
         return render(request, "wordList/card_form.html", {"form": form})
      elif "delete" in request.POST:
         card.delete()
         return redirect('wordList:card_list')



index = IndexView.as_view()
card_create = CardCreateView.as_view()
card_list = CardListView.as_view()
card_update = CardUpdateView.as_view()