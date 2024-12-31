import requests
from bs4 import BeautifulSoup

class WordSearch():
   def word_search(self, search_word):
      url = 'https://ejje.weblio.jp/content/'
      response = requests.get(url + search_word)
      print('got')

      soup = BeautifulSoup(response.text, 'html.parser')

      try:
         return soup.select('div.summaryM.descriptionWrp span.content-explanation.ej')[0].text.strip()
      except:
         return 'Not Found'
      