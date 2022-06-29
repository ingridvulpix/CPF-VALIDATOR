from tkinter import *
from cpf import Cpf
from cnpj import Cnpj

class Interface(Cpf,Cnpj):
    def __init__(self, root):
        self.root = root
        self.message =''''''
        self.var_cpf = StringVar()
        self.var_cnpj = StringVar()
        self.cpf_aux = list(range(10,1,-1)) #vector for dot product
        self.cpf_aux_2 = list(range(11,1,-1)) #vector for dot product
        self.create_canvas()
    
    def create_canvas(self):
        self.root.title('CPF/CNPJ validator')
        self.root.geometry('700x250')
        self.frame_cpf = Frame(self.root)
        self.frame_cpf.pack()
        self.frame_cnpj = Frame(self.root)
        self.frame_cnpj.pack()
        self.create_label()
        self.create_text_box_cpf()
        self.create_text_box_cnpj()
    
    def extract_data_cpf(self):
        self.cpf = (self.text_cpf.get('1.0', 'end')).strip()
        self.dv_cpf = int((self.text_cpf_dv.get('1.0', 'end')).strip())
        self.validation_output_cpf()
        self.reset_btn()

    def extract_data_cnpj(self):
        self.cnpj = (self.text_cnpj.get('1.0', 'end')).strip()
        self.dv_cnpj = int((self.text_cnpj_dv.get('1.0', 'end')).strip())
        self.validation_output_cnpj()
        self.reset_btn()
        
    def create_label(self):
        self.label_cpf = Label( self.frame_cpf, textvariable=self.var_cpf, padx=10,relief=RAISED, font=("Ubuntu",12))
        self.var_cpf.set("Please, insert the first 9 digits of your CPF in the first box,\n \
            and then insert the last 2 digits in the second box")
        self.label_cpf.pack()
        self.label_cnpj = Label( self.frame_cnpj, textvariable=self.var_cnpj, relief=RAISED, font=("Ubuntu",12))
        self.var_cnpj.set("Please, insert the first 12 digits of your CNPJ in the first box,\n \
            and then insert the last 2 digits in the second box")
        self.label_cnpj.pack()
    
    def create_text_box_cpf(self):
        self.text_cpf = Text(self.frame_cpf,height=1,width=13,wrap='word')
        self.text_cpf_dv = Text(self.frame_cpf,height=1,width=2,wrap='word')
        self.text_cpf.pack(padx=15, pady=10,side='left')
        self.text_cpf_dv.pack(padx=5, pady=10,side='left')
        self.text_cpf.insert('end', self.message)
        self.text_cpf_dv.insert('end', self.message)
        self.create_button_cpf()

    def create_text_box_cnpj(self):
        self.text_cnpj = Text(self.frame_cnpj,height=1,width=16,wrap='word')
        self.text_cnpj_dv = Text(self.frame_cnpj,height=1,width=2,wrap='word')
        self.text_cnpj.pack(padx=15, pady=10,side='left')
        self.text_cnpj_dv.pack(padx=5, pady=10,side='left')
        self.text_cnpj.insert('end', self.message)
        self.text_cnpj_dv.insert('end', self.message)
        self.create_button_cnpj()

    def create_button_cpf (self):
            self.button_cpf = Button(self.frame_cpf,text='Validate CPF',command= self.extract_data_cpf)
            self.button_cpf.pack(padx=5, pady=15,side='left')
            self.generate_bttn_cpf = Button(self.frame_cpf,text='Generate CPF',command= self.random_cpf )
            self.generate_bttn_cpf.pack(padx=5, pady=15,side='left')
    
    def create_button_cnpj (self):
            self.button_cnpj = Button(self.frame_cnpj,text='Validate CNPJ',command= self.extract_data_cnpj)
            self.button_cnpj.pack(padx=5, pady=15,side='left')
            self.generate_bttn_cnpj = Button(self.frame_cnpj,text='Generate CNPJ',command= self.random_cnpj )
            self.generate_bttn_cnpj.pack(padx=5, pady=15,side='left')

    def random_cpf(self):
        self.text_cpf.config(state = DISABLED)
        self.text_cpf_dv.config(state = DISABLED)
        new_cpf = self.generate_cpf()
        self.generate_output_cpf = Text(self.frame_cpf, height=1,width=15, bg='#2499d7')
        self.generate_output_cpf.insert('end',new_cpf)
        self.generate_output_cpf["state"] = DISABLED
        self.generate_output_cpf.pack(padx=10, pady=15, side='left')
        self.reset_btn()

    def random_cnpj(self):#FIXME cannot generate cnpj
        self.text_cnpj.config(state = DISABLED)
        self.text_cnpj_dv.config(state = DISABLED)
        new_cnpj = self.generate_cnpj()
        self.generate_output_cnpj = Text(self.frame_cnpj, height=1,width=15, bg='#2499d7')
        self.generate_output_cnpj.insert('end',new_cnpj)
        self.generate_output_cnpj["state"] = DISABLED
        self.generate_output_cnpj.pack(padx=10, pady=15, side='left')
        self.reset_btn()

    def reset_btn(self):
        self.button_cpf.config(state = DISABLED)
        self.generate_bttn_cpf.config(state = DISABLED)
        self.button_cnpj.config(state = DISABLED)
        self.generate_bttn_cnpj.config(state = DISABLED)
        self.refresh_button = Button(self.frame_cpf, text='Refresh', command= self.clear).pack(padx=5, pady=15,side='left')
        self.refresh_button = Button(self.frame_cnpj, text='Refresh', command= self.clear).pack(padx=5, pady=15,side='left')

    def validation_output_cpf(self):
        valid = self.areValidDigitsCpf(False)
        text = 'Valid CPF'if valid == True else 'Invalid CPF'
        bg_color = '#bef9e2' if valid == True else '#ff5555'
        self.output_text_cpf = Text(self.frame_cpf, height=1,width=11, bg=bg_color)
        self.output_text_cpf.insert('end',text)
        self.output_text_cpf["state"] = DISABLED
        self.output_text_cpf.pack(padx=10, pady=15, side='left')

    def validation_output_cnpj(self):#FIXME cannot validate cnpj
        valid = self.areValidDigitsCnpj(False)
        text = 'Valid CNPJ'if valid == True else 'Invalid CNPJ'
        bg_color = '#bef9e2' if valid == True else '#ff5555'
        self.output_text_cnpj = Text(self.frame_cnpj, height=1,width=11, bg=bg_color)
        self.output_text_cnpj.insert('end',text)
        self.output_text_cnpj["state"] = DISABLED
        self.output_text_cnpj.pack(padx=10, pady=15, side='left')

    def clear(self):
        self.frame_cpf.destroy()
        self.frame_cnpj.destroy()
        self.create_canvas()