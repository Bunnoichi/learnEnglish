from django.urls import path
from . import views


app_name = 'wordList'
urlpatterns = [
   path("", views.index, name="index"),
   path("card/create/", views.card_create, name="card_create"),
   path("card/list/", views.card_list, name="card_list"),
   path("card/<uuid:id>/update", views.card_update, name="card_update"),

]