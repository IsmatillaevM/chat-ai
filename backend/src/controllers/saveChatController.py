

import json
import sqlite3
import time



class saveChatClass:
    @staticmethod
    def saveSql(chatlist:list):
        gettime=time.strftime("%Y-%m-%d", time.localtime())
        conn = sqlite3.connect('./src/data/chat.db')
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS questionAnswer (question TEXT, answer TEXT, bleau TEXT, time TEXT )')
        for chat in chatlist:
            cursor.execute('INSERT INTO questionAnswer (question, answer,bleau, time) VALUES (?,?,?,?)',(chat['question'],chat['answer'], chat['bleau'], gettime))

        conn.commit()
        conn.close()

    @staticmethod
    def getHistory()->dict:
        conn = sqlite3.connect('./src/data/chat.db')
        cursor=conn.cursor()

        db=cursor.execute('select * from questionAnswer')
    
        
        return  [{

            'question':row[0],

            'answer':row[1],

            'time':row[2],

        
        } for row in db]





