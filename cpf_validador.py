from tkinter import *
from tkinter import messagebox


class Interface:
    def __init__(self, root):
        self.root = root
        self.create_canvas()
    
    def create_canvas(self):
        self.root.title('APX3_PIG')
        self.root.geometry('300x150')
        self.root.config(bg = 'gray')
        self.create_text_box()
    
    def extract_data(self):
        self.data = self.text_box.get('1.0', 'end')
        print(self.data)
    
    def create_text_box(self):
        self.message =''''''

        self.text_box = Text(
            self.root,
            height=1,
            width=20,
            wrap='word'
        )
        self.text_box.pack(expand=True)
        self.text_box.insert('end', self.message)
        self.create_button()

    def create_button (self):
        Button(
        self.root,
        text='Validate CPF',
        command= self.extract_data
    ).pack(expand=True)
        self.inside()

    def inside (self):
        self.root.mainloop()

if __name__== '__main__':

    ws = Tk()
    user_cpf = Interface(ws)