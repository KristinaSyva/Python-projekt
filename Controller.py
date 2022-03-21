#user first sends the requests to controller, handles the request flow; should not contain much code
# 1. controller asks from Model information based on the request
# Controller never handles data logic
# Controller gets data from Model and sends to view

from tkinter import messagebox
import tkinter
from Model import *
from View import *


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.show_words()
        
    def main(self):
        self.view.main() 
        
        
    def btn_del_click(self):
        content = self.view.textbox.selection_get()
        s0 = self.view.textbox.index("sel.first")
        s1 = self.view.textbox.index("sel.last")
        ''' print(s0) #starting row
        print(s1) #ending row 
        lines = self.view.textbox.get("1.0", tkinter.END).splitlines()
        print(lines)
        ''' 
        print(s0)
        print(s1)
        index = s0.split('.')[0]
        #index = s0[0]
        self.model.delete(content)
        self.update()
        messagebox.showinfo('Teade','Kirje on kustutatud!') 
        #self.model.insert()
        
    def show_words(self):
        self.model.get_all_words()
        arr = self.model.words
        result = ""
        for i in arr:
            #print(i, end = ' ')
            result+=(i[0]+"\n")

        self.view.textbox.insert(INSERT, result)
        self.view.textbox.configure(state='disabled')
        
    def btn_add_click(self):
       self.model.insert(self.view.userinput)  
       self.update()
       pass
   
    def update(self):
       self.view.textbox.configure(state='normal')
       self.view.textbox.delete('1.0', END)
       self.show_words()
       self.view.textbox.configure(state='disabled')
