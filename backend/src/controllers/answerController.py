from transformers import BertForQuestionAnswering, AutoTokenizer,pipeline


modelname = 'deepset/bert-base-cased-squad2'

model = BertForQuestionAnswering.from_pretrained(modelname)
tokenizer = AutoTokenizer.from_pretrained(modelname)


nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)




class answerClass:
    def answer(question):
        
        return  {
          
          'answer':  nlp({
            
            'question':question,

            
            'context':answerClass.read()
            
                        })['answer'],

          'context':answerClass.read()
        }
    

    def read():
        with open ('./src/data/python.txt','r') as f:
            return f.read()
        
        
    
    