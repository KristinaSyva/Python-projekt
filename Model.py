# Model is responsible for data logic 
# Model interacts with a database: saving, updating, deleting etc.
# Nodel does not have to worry about user request or what to do in case of failiure or sucess
# Model sends data to Controller
#any interaction between Model and View go through Controller

import sqlite3

class Model:
    
    def __init__(self):
        self.database_name = 'words.db' 
        self.words = [] 
        
    def get_all_words(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.execute('SELECT word FROM words')
        self.words = cursor.fetchall()
        connection.close()

    def delete(self, word):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        sql = "DELETE FROM words WHERE word = '"+word+"'"
        cursor.execute(sql)
        print(sql)
        connection.commit()
        connection.close()
        
    def insert(self, word):
        resstring = word.get()
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        sql_insert_query = " INSERT INTO words (word, category) VALUES ('"+resstring+"','Amet')"
        print(sql_insert_query)
        # tuple to insert at placeholder
        cursor.execute(sql_insert_query)
        connection.commit()        
        connection.close()

#.commit() sellega saab andmeid lisada andmebaasi
