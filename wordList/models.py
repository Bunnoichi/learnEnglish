from django.db import models
import uuid

class Card(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
   word = models.CharField(max_length=50, verbose_name="単語")
   meaning = models.CharField(max_length=200, verbose_name="意味")
   note = models.TextField(blank=True, verbose_name="備考")
   created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

   def __str__(self):
      return self.word