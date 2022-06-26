from tkinter import *
import tkinter as tk
import sys
from operator import mul
class CPF:
    def __init__(self,cpf:str, dv:int):
        self.cpf = cpf
        self.dv = dv
        self.cpf2 = list(range(10,1,-1))
        self.getDigits()
    
    def getDigits (self):
        return list(map(int,filter(lambda x:x.isdecimal(),self.cpf )))


    def dotProd (self, v1:list[int], v2:list[int]):
        return sum(map(mul, v1, v2))

    def areValidDigits (self):
        cpf1 = self.getDigits()
        dv2 = self.dotProd(cpf1,self.cpf2)
        result = dv2 % 11
        dv2 = 0 if result <= 1 else 11 - result
        self.cpf2 = list(range(11,1,-1))
        cpf1.append(dv2)
        dv1 = self.dotProd(cpf1,self.cpf2)
        result = dv1 % 11
        dv1 = 0 if result <= 1 else 11 - result
        print ((dv2*10 + dv1 == self.dv))
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