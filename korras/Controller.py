import tkinter as tk
from tkinter import simpledialog
from Model import *
from View import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        
    def main(self):
        self.view.main() #View.py failis olev main meetod
        
        
    def btn_new_click(self):
        'uus mäng nupp vajutatud'
        #print('klikiti uus mäng nupp')
        self.model.set_new_game()
        self.view.label.configure(text=self.model.user_word, bg='yellow')
        self.view.label_error.configure(text=f'Valesti 0 täht(e)',fg='black')
        self.view.button['state'] = NORMAL
    
    def btn_send_click(self): #see näitab valede tähtede listi
        'iga nupu Saada vajutus, suurendab vajadusel numbrit, tühjendab välja'
        self.model.get_user_input(self.view.userinput.get().strip())
        self.view.label.configure(text=self.model.get_user_word())
        self.view.label_error.configure(text=f'Valesti {self.model.get_counter()} täht(e). {self.model.get_all_user_chars()}')
        self.view.char_input.delete(0, 'end') # tühjendab entry välja
        if self.model.get_counter() >= 1:
            self.view.label_error.configure(fg='red')
        self.is_game_over()
   
    def is_game_over(self):
        if self.model.get_counter() >= 8 or '_' not in self.model.get_user_word():
            #messagebox.showinfo('Teade','Mäng on läbi') #1. teade 2. sisu
            self.view.button['state'] = DISABLED
            #kysida nime ja siin sees teha failiga seotud operatsioonid
            player_name = simpledialog.askstring("Mäng läbi", "Mis on su nimi?\nKuidas mäng meeldis")
            self.model.set_username(player_name)
            
    def btn_scoreboard_click(self):
        popup_frame = self.view.create_popup_window()
        data = self.model.read_file_contents() #loe faili sisu Listi
        self.view.generate_scoreboard(popup_frame, data) # nõuab frame ja andmeid
        