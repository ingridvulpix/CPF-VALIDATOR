from tkinter import *
from cpf import Cpf
from cnpj import Cnpj
from interface import Interface

if __name__== '__main__':

        ws = Tk()
        user_cpf = Interface(ws)
        ws.mainloop()