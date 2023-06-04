# Bismillah

from flask import Flask , request

from flask_cors import CORS


from src.controllers.translateQuestionController import translateQuestionClass
from src.controllers.saveChatController import saveChatClass




import json



app = Flask(__name__)
CORS(app)


# этот метод запускает контроллер translateQuestionClass и возвращает ответ
@app.route('/getAnswer',methods=['GET', 'POST'])
def getAnswer():

        query=json.loads(request.data)


        question=query['question']

        typeanswer=query['typeanswer']

        return json.dumps(translateQuestionClass.translate(question,typeanswer))







@app.route('/saveChatDb',methods=['GET', 'POST'])
def saveChatDb():

        query=json.loads(request.data)


        chatlist=query['chatlist']

        saveChatClass.saveSql(chatlist)
        

        return json.dumps('ok')



@app.route('/getHistory',methods=['GET', 'POST'])
def getAnswers():

        
        return json.dumps(saveChatClass.getHistory())



if  __name__  == '__main__' :
        app.run()