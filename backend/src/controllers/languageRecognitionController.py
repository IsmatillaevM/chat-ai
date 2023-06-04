# import fasttext

class languageRecognitionClass:
    # метод определяет язык вопроса
    @staticmethod
    def languageRecognition(text:str)->str:
        
        pretrained_lang_model = "./src/models/lid.176.bin"
        
        model = fasttext.load_model(pretrained_lang_model)
        
        predictions = model.predict(text, k=1)
        print(predictions[0][0].replace("__label__", ""))
        return predictions[0][0].replace("__label__", "")

        


