# siin failis toimub anmdete muutmine
import sqlite3
from datetime import datetime
from Score import *

class Model:
    
    def __init__(self):
        self.database_name = 'words.db' # andmebaasi nimi
        self.new_word = None # sõna mida ära arvatakse
        self.user_word = [] #kasutaja leitud tähed
        self.all_user_chars = [] # valesti sisestatud tähed
        self.counter = 0 #vigade loendus
        self.player_name = "TEADMATA"
        self.score_filename = 'score.txt'
        self.score_date = [] #score.txt faili sisu on siin sees
        
    def get_random_word(self):
        'Üks juhuslik sõna tabelist'
        connection = sqlite3.connect(self.database_name)
        cursor = connection.execute('SELECT * FROM words ORDER BY RANDOM() LIMIT 1')
        self.new_word = cursor.fetchone()[1] #veerg word on [1] ja id on [0]
        connection.close()
        
    def set_new_game(self):
        'Tee uus mäng'
        self.get_random_word()
        self.user_word = []
        self.all_user_chars = [] #valesti sisestatud tähed eemaldada
        self.counter = 0
        for i in range (len(self.new_word)):
            self.user_word.append('_')
            #print(self.new_word)
            #print(self.user_word)
            
    def get_user_input(self, value):
        'mida kasutaja sisestab'
        if value: #kas kasutaja on midagi sisestanud ja see pole tühi
            user_char = value[0:1] # esimene märk
            if user_char.lower() in self.new_word.lower():
                self.change_user_input(user_char)
            else: #ei leitud
                self.counter += 1 #vigade loendur pluss 1
                self.all_user_chars.append(user_char.upper())
                
    def change_user_input(self, user_char):
        current_word = self.chars_to_list(self.new_word)
        i=0
        for c in current_word:
            if user_char.lower() == c.lower():
                self.user_word[i] = user_char.upper()
            i += 1
            
    
    def chars_to_list(self, string):
        chars=[]
        chars[:0]=string
        return chars
    
    def get_user_word(self):
        'Tagastab kasutaja leitud tähed'
        return self.user_word
    
    def get_counter(self):
        return self.counter
    
    def get_all_user_chars(self):
        return ', '.join(self.all_user_chars) # join ühendab listi, eemaldab [] kantsukud aga ka tühikud ja komad, sellepärast lisame juurde koma ja tühiku
    
    def set_player_name(self):
        self.player_name = "TEADMATA"
        
        
    def set_username(self, username):
        line = []
        now = datetime.now().strftime('%Y-%m-%d %T')
        if username:
            self.player_name = username
            
        line.append(now)
        line.append(self.player_name)
        line.append(self.new_word)
        line.append(self.get_all_user_chars())
        
        with open(self.score_filename, 'a+', encoding='utf-8') as f:
            f.write(';'.join(line) + '\n')
            
    def read_file_contents(self):
        self.score_data = []
        with open(self.score_filename, 'r', encoding='utf-8') as f: #avan faili; utf-8 sisaldab täpitähti
            all_lines = f.readlines() #loe faili sisu listi
            for line in all_lines:
                parts = line.strip().split(';') #strip eemaldab tühikuid ja entereid; split ütleb mille juurest lahti ühendada
                self.score_data.append(Score(parts[0],parts[1],parts[2],parts[3]))
            print(self.score_data[0].get_date())
        return self.score_data 