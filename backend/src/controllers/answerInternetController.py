from serpapi import GoogleSearch

import requests

from bs4 import BeautifulSoup
    
 


class answerInternetClass:
#  Функция search возвращает результаты поиска по запросу query, 
    @staticmethod
    def answerInternet(question:str) -> dict:
        #  params - параметры поиска в поисковых системах
        params={
        
        'q': {question},
         
         'serp_api_key': '47f4fa37bc3bb3e8c840af606837fe42351d838957fb53cdff5fef0bb100106f'
         
         }

        link=GoogleSearch(params).get_dict()['organic_results'][:1][0]['link']
        return  answerInternetClass.scrape(link)

    
    #  Функция scrape возвращает текстовое содержимое страницы по ссылке link, 
    @staticmethod
    def scrape(link:str)->list:
        sentences=[]
        try:
            reqs = requests.get(link)
            soup = BeautifulSoup(reqs.text,'html.parser')

            for heading in soup.find_all([ 'p']):
                if len(sentences)<5:
                    if heading.text.replace('\n', ' ')!='':
                        sentences.append(heading.text.replace('\n', ' '))
        except requests.exceptions.ConnectionError:
                sentences.append('not craw')

        if len(sentences)==0:
            sentences.append('not craw')
        
       
        return {
            
            'answer':' '.join(sentences),

            'context':' '.join(sentences),
            
                }




       

                
    
            


    



