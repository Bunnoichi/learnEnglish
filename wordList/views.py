from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Card
from .forms import CardForm
from .wordsearch import WordSearch

class IndexView(View):
   def get(self, request):
      return render(request, "wordList/index.html")
   
class CardCreateView(View):
   def get(self, request):
      form = CardForm()
      return render(request, "wordList/card_form.html", {"form": form})
       
   def post(self, request):
      form = CardForm(request.POST)
      print(request.POST)
      print(type(request))
      if "create" in request.POST:
         if form.is_valid():
            form.save()
         return render(request, "wordList/card_form.html", {"form": CardForm(None)})
      elif "search" in request.POST:
         form = CardForm(request.POST)
         # found_meaning = form.fields['word']
         # found_meaning = request.POST['word']
         return render(
            request, 
            "wordList/card_form.html", 
            {"form": form, 
             "foundmeaning": WordSearch().word_search(request.POST['word'])
             })

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

class LessonSessionView(View):
   def get(self, request):
      card = Card.objects.order_by('?')[0]
      print(card)
      return render(request, "wordList/lesson_session.html", {"card": card})
   
   def post(self, request):
      data = Card.objects.get(pk=request.POST['id'])

      try:
         data.count_appear += 1
      except:
         data.count_appear = 0
         data.count_appear += 1
         data.count_incorrect = 0

      if "incorrect" in request.POST:
         data.count_incorrect += 1
      
      data.save()

      card = Card.objects.order_by('?')[0]
      return render(request, "wordList/lesson_session.html", {"card": card})

index = IndexView.as_view()
card_create = CardCreateView.as_view()
card_list = CardListView.as_view()
card_update = CardUpdateView.as_view()
lesson_session = LessonSessionView.as_view()