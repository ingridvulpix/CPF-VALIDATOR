from tkinter import *
import tkinter as tk
from cpf import Cpf

class Interface(Cpf):
    def __init__(self, root):
        self.root = root
        self.message =''''''
        self.var = StringVar()
        self.cpf_aux = list(range(10,1,-1))
        self.create_canvas()
    
    def create_canvas(self):
        self.root.title('APX3_PIG')
        self.root.geometry('500x150')
        self.root.config(bg = 'gray')
        self.frame = Frame(self.root)
        self.frame.pack()
        self.create_label()
        self.create_text_box()
    
    def extract_data(self):
        self.cpf = (self.text_cpf.get('1.0', 'end')).strip()
        self.dv = int((self.text_dv.get('1.0', 'end')).strip())
        self.validation_output()
        self.reset_btn()
        
    def create_label(self):
        self.label = Label( self.frame, textvariable=self.var, relief=RAISED, font=("Ubuntu",12))
        self.var.set("Please, insert the first 9 digits of your CPF in the first box,\n \
            and then insert the last 2 digits in the second box")
        self.label.pack()
    
    def create_text_box(self):
        self.text_cpf = Text(self.frame,height=1,width=13,wrap='word')
        self.text_dv = Text(self.frame,height=1,width=2,wrap='word')
        self.text_cpf.pack(padx=15, pady=10,side='left')
        self.text_dv.pack(padx=5, pady=10,side='left')
        self.text_cpf.insert('end', self.message)
        self.text_dv.insert('end', self.message)
        self.create_button()

    def create_button (self):
            self.button = Button(self.frame,text='Validate CPF',command= self.extract_data)
            self.button.pack(padx=5, pady=15,side='left')

    def reset_btn(self):
        self.button.config(state = DISABLED)
        self.refresh_button = Button(self.frame, text='Refresh', command= self.clear).pack(padx=5, pady=15,side='left')

    def validation_output(self):
        valid = self.areValidDigits()
        text = 'Valid CPF'if valid == True else 'Invalid CPF'
        bg_color = '#bef9e2' if valid == True else '#ff5555'
        self.output_text = Text(self.frame, height=1,width=11, bg=bg_color)
        self.output_text.insert('end',text)
        self.output_text["state"] = DISABLED
        self.output_text.pack(padx=10, pady=15, side='left')


    def clear(self):
        self.frame.destroy()
        self.create_canvas()


if __name__== '__main__':

        ws = Tk()
        user_cpf = Interface(ws)
        ws.mainloop()