import datetime
from datetime import datetime
from tkinter import *
from tkinter import ttk #scrollbar tuleb siit
import tkinter.font as tkFont

class View(Tk): #Tk tuleb tkinterist, kui seda siin ei ole siis super rida 7 oleks tundmatu
    
    def __init__(self, controller):
        super().__init__() #Tk jaoks
        #mõned muutujad
        self.controller = controller
        self.userinput=StringVar()
        self.bigFontStyle = tkFont.Font(family='Courier', size=18, weight='bold')
        self.defaultStyle = tkFont.Font(family='Verdana', size=10)
        self.defaultStyleBold = tkFont.Font(family='Verdana', size=10, weight='bold')
        
        #Põhiaken
        self.geometry('450x200') # akna suurus
        self.resizable(1,1) #või True, True; akna suurust saab muuta
        self.title('Hangman')
        
        #Framed kutsutakse välja
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()
        
        #Vidinad / konstruktor
        self.create_new_button() # nupp
        self.create_popup_button() #edetabeli nupp
        self.char_input, self.label_error, self.button = self.create_userinput()
        self.label = self.create_result_label()
        
    def main(self):
        self.mainloop()
        
    #Framede tegemine
    def create_top_frame(self):
        frame = Frame(self, bg='blue', height=50) #sulgudes peab olema mille peale raam tehakse, siin iseenda peale
        frame.pack(expand = True, fill ='both')
        return frame
    
    def create_bottom_frame(self):
        frame = Frame(self, bg='yellow') #sulgudes peab olema mille peale raam tehakse, siin iseenda peale
        frame.pack(expand = True, fill ='both')
        return frame
    
    def create_new_button(self):
        button = Button(self.top_frame, text='Uus mäng', font=self.defaultStyle, command=lambda:self.controller.btn_new_click())
        button.grid(row=0,column=0, padx=5, pady=5, sticky=EW) #EW-east west
        
        
        
        
    def create_userinput(self):
        label_info = Label(self.top_frame, text='Sisesta täht', font=self.defaultStyleBold)
        label_info.grid(row=1, column=0, padx=5, pady=5)
        
        char_input = Entry(self.top_frame, textvariable=self.userinput, justify='center', font=self.defaultStyle)
        char_input.grid(row=1,column=1, padx=5, pady=5)
        char_input.focus()
        
        button = Button(self.top_frame, text='Saada', state='disabled', font=self.defaultStyle, command=lambda:self.controller.btn_send_click())
        button.grid(row=1, column=2, padx=5, pady=5)
        button['state'] = DISABLED
        
        label_error =Label(self.top_frame, text='Valesti 0 täht(e)', anchor='w', font=self.defaultStyle)
        label_error.grid(row=2, column=0, columnspan=3, sticky=EW, padx=5, pady=5)
        
        return char_input, label_error, button
    
    
    def create_result_label(self):
        label = Label(self.bottom_frame, text="HAKKAME MÄNGIMA", font=self.bigFontStyle)
        label.pack(padx=5,pady=5)
        return label
    
    #popup osa
    def create_popup_button(self):
        button = Button(self.top_frame, text='Ededabel', font=self.defaultStyle, command=lambda:self.controller.btn_scoreboard_click())
        button.grid(row=0, column=1,padx=5, pady=5, sticky=EW)
        
    def create_popup_window(self):
        top = Toplevel(self) #tehakse olemasoleva akna peale
        top.geometry('500x150')
        top.title('Edetabel')
        top.resizable(0,0) #ei saa muuta
        top.grab_set()#modal
        top.focus() #et oleks aktiivne
        frame = Frame(top)
        frame.pack(expand=True, fill='both')
        return frame
    
    def generate_scoreboard(self, frame, data):
        my_table = ttk.Treeview(frame) #treeview tehakse frame peale
        
        #vertikaalne scrollbar
        vsb = ttk.Scrollbar(frame, orient='vertical', command=my_table.yview)
        vsb.pack(side='right', fill='y') #täida ülevalt alla
        my_table.configure(yscrollcommand=vsb.set)
        
        #veeru nö ID
        my_table['columns'] = ('date_time', 'player_name', 'word', 'misses')
        
        #veeru omadused
        my_table.column('#0',width=0,stretch=NO) # mingi tühi asi
        my_table.column('date_time', anchor=CENTER, width=80)
        my_table.column('player_name', anchor=CENTER, width=80)
        my_table.column('word', anchor=CENTER, width=80)
        my_table.column('misses', anchor=CENTER, width=80)
        
        #veeru pealkirjad
        my_table.heading('#0', text='', anchor=CENTER) 
        my_table.heading('date_time', text='Kuupäev', anchor=CENTER) 
        my_table.heading('player_name', text='Mängija', anchor=CENTER) 
        my_table.heading('word', text='Sõna', anchor=CENTER) 
        my_table.heading('misses', text='Vigased tähed', anchor=CENTER) 
        
        #andmete lisamine
        i = 0
        for p in data: #p on mängija nimi
            dt = datetime.strptime(p.get_date(), "%Y-%m-%d %H:%M:%S").strftime('%d.%m.%Y %T') # dt siin tähendab datetime
            my_table.insert(parent='', index='end', iid=i, text='', values=(dt,p.get_name(),p.get_word(),p.get_misses())) ###get_date muuta
            i += 1

        my_table.pack(expand=True, fill='both') # asjad pannakse reaalselt frame peale 




