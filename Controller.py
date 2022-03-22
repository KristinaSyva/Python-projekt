from tkinter import messagebox
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
        print(s0)
        print(s1)
        index = s0.split('.')[0]
        self.model.delete(content)
        self.update()
        messagebox.showinfo('Teade','Kirje on kustutatud!') 


    def show_words(self):
        self.model.get_all_words()
        arr = self.model.words
        result = ""
        for i in arr:
            result+=(i[0]+"\n")
        self.view.textbox.insert(INSERT, result)
        self.view.textbox.configure(state='disabled')


    def btn_add_click(self):
       self.model.insert(self.view.userinput)  
       self.update()

   
    def update(self):
       self.view.textbox.configure(state='normal')
       self.view.textbox.delete('1.0', END)
       self.show_words()
       self.view.textbox.configure(state='disabled')
