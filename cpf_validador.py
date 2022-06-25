from tkinter import *
import tkinter as tk


class Interface:
    def __init__(self, root):
        self.root = root
        self.message =''''''
        self.create_canvas()
    
    def create_canvas(self):
        self.root.title('APX3_PIG')
        self.root.geometry('300x150')
        self.root.config(bg = 'gray')
        self.create_text_box()
    
    def extract_data(self):
        self.data_cpf = (self.text_cpf.get('1.0', 'end')).strip()
        self.data_dv = (self.text_dv.get('1.0', 'end')).strip()
        data = [self.data_cpf,self.data_dv]
    
    def create_text_box(self):
        
        self.text_cpf = Text(
            self.root,
            height=1,
            width=9,
            wrap='word'
        )
        self.text_dv = Text(
            self.root,
            height=1,
            width=2,
            wrap='word'
        )
        self.text_cpf.pack(side=tk.LEFT, expand=TRUE)
        self.text_dv.pack(side=tk.LEFT, expand=TRUE)
        self.text_cpf.insert('end', self.message)
        self.text_dv.insert('end', self.message)
        self.create_button()

    def create_button (self):
        Button(
        self.root,
        text='Validate CPF',
        command= self.extract_data
    ).pack(expand=TRUE)
        self.inside()

    def generate_valid_cpf (self):
        #call the other class to get valid cpf
        self.message = '''757.331.783-29'''

    def inside (self):
        self.root.mainloop()

if __name__== '__main__':

    ws = Tk()
    user_cpf = Interface(ws)