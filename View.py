from tkinter import *
import tkinter.font as tkFont

class View(Tk): 
    
    def __init__(self, controller):
        super().__init__() 
        self.controller = controller
        self.userinput=StringVar()
        self.defaultStyle = tkFont.Font(family='Helvetica', size=10, weight='bold')        
        self.geometry('450x450') 
        self.resizable(0,0) 
        self.title('Andmebaasi uuendamine')
        
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()
        
        self.delete_button()
        self.char_input, self.button = self.create_userinput()
        self.textbox = self.create_database_textbox()


    def main(self):
        self.mainloop()


    def create_top_frame(self):
        'nupud ja sisestus'
        frame = Frame(self, height=50)
        frame.pack(expand = False, fill = X)
        return frame


    def create_bottom_frame(self):
        'andmebaasi info kuvamiseks'
        frame = Frame(self) 
        frame.pack(expand = True, fill ='both')
        return frame


    def create_userinput(self):
        label_info = Label(self.top_frame, text='Uus amet andmebaasi:', font=self.defaultStyle)
        label_info.grid(row=1, column=0, padx=5, pady=5)
        
        label_info2 = Label(self.top_frame, text='Tee sõna aktiivseks ja:', font=self.defaultStyle)
        label_info2.grid(row=2, column=1, padx=5, pady=5)
        
        char_input = Entry(self.top_frame, textvariable=self.userinput, justify='center', font=self.defaultStyle)
        char_input.grid(row=1,column=1, padx=5, pady=5)
        char_input.focus()
        
        button = Button(self.top_frame, text='Lisa!', font=self.defaultStyle, borderwidth = 2, bg='gray', fg='white', command=lambda:self.controller.btn_add_click())
        button.grid(row=1, column=2, padx=5, pady=5)

        return char_input, button
    
    
    def delete_button(self):
        'Kustuta nupp'
        button = Button(self.bottom_frame, text='KUSTUTA!', font=self.defaultStyle, borderwidth = 2, bg='gray', fg='white', command=lambda:self.controller.btn_del_click())
        button.pack(padx=5,pady=5)


    def create_database_textbox(self):
        'Andmebaasi kuvamine'
        textbox = Text(self.bottom_frame, borderwidth = 0)
        textbox.pack(padx=5,pady=5)
        return textbox