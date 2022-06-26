from tkinter import *
import tkinter as tk
import sys
from operator import mul

global end_run
end_run = False
class Legal_number:
    def __init__(self,cpf:str, dv:int):
        self.cpf = cpf
        self.dv = dv
        self.getDigits()
    
    def getDigits (self):
        return list(map(int,filter(lambda x:x.isdecimal(),self.cpf )))

    def dotProd (self, v1:list[int], v2:list[int]):
        return sum(map(mul, v1, v2))

    def areValidDigits (self):
        cpf1 = self.getDigits()
        dv2 = self.dotProd(cpf1,self.cpf_aux)
        result = dv2 % 11
        dv2 = 0 if result <= 1 else 11 - result
        self.cpf_aux_2 = list(range(11,1,-1))
        cpf1.append(dv2)
        dv1 = self.dotProd(cpf1,self.cpf_aux_2)
        result = dv1 % 11
        dv1 = 0 if result <= 1 else 11 - result
        return (dv2*10 + dv1 == self.dv)

class Interface(Legal_number):
    def __init__(self, root):
        self.root = root
        self.message =''''''
        self.cpf_aux = list(range(10,1,-1))
        self.create_canvas()
    
    def create_canvas(self):
        self.root.title('APX3_PIG')
        self.root.geometry('500x150')
        self.root.config(bg = 'gray')
        self.frame = Frame(self.root)
        self.frame.pack()
        self.create_text_box()
    
    def extract_data(self):
        self.cpf = (self.text_cpf.get('1.0', 'end')).strip()
        self.dv = int((self.text_dv.get('1.0', 'end')).strip())
        self.validation_output()
        self.reset_btn()
        
    
    def create_text_box(self):
        
        self.text_cpf = Text(
            self.frame,
            height=1,
            width=13,
            wrap='word'
        )
        self.text_dv = Text(
            self.frame,
            height=1,
            width=2,
            wrap='word'
        )
        self.text_cpf.pack(padx=15, pady=10,side='left')
        self.text_dv.pack(padx=5, pady=10,side='left')
        self.text_cpf.insert('end', self.message)
        self.text_dv.insert('end', self.message)
        self.create_button()

    def create_button (self):
            self.button = Button(
            self.frame,
            text='Validate CPF',
            command= self.extract_data
        )
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