from googletrans import Translator

from src.controllers.languageRecognitionController import languageRecognitionClass

from src.controllers.answerController import answerClass
from src.controllers.answerInternetController import answerInternetClass
from src.controllers.accuracyController import accuracyClass
from src.controllers.bleauController import bleauClass


class translateQuestionClass:
    # метод переводит вопрос на английский и возвращает ответ
    @staticmethod
    def translate(question:str,typeanswer)->str:

        translator = Translator()
        # # определяем язык вопроса,запускается контроллер languageRecognitionController
        # typelanguage=languageRecognitionClass.languageRecognition(question)

        # переводим вопрос на английский
        translatedText = translator.translate(

            question, 
            
            # src= typelanguage,
            
            dest='en'
            
                 ).text
        

        if(typeanswer=='internet'):
            getanswer=answerInternetClass.answerInternet(translatedText)
        
        elif(typeanswer=='local'):
            getanswer=answerClass.answer(translatedText)
            
            
            

            

           
        
        
        # переводим ответ на язык вопроса
        
        return {

            'answer':translator.translate(

            getanswer['answer'], 
            
            src= 'en',
            
            # dest= typelanguage
            
                 ).text,
                 

            # 'accuracy':accuracyClass.calculate_accuracy(translatedText,getanswer['answer']),

            'bleau':bleauClass.calculate_bleu_score(translatedText,getanswer['answer'],getanswer['context'])
            
        }




