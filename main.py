from tkinter import *

class Imc:
    def __init__(self):
        #Criação de janela do tkinter
        self.root = Tk()
        self.root.title('Calculadora de IMC')
        self.root.resizable(0, 0)
        self.root.geometry('320x240+300+250')

        #Container que irá abrigar campo peso
        self.frame1 = Frame(self.root)
        self.frame1.pack(padx=4, pady=4)

        #Descrição e campo de entrada para o peso
        self.peso_desc = Label(self.frame1, text='Informe seu peso', font='Arial 12 bold')
        self.peso_desc.pack(side='left')
        self.peso = Entry(self.frame1, width=5)
        self.peso.pack(side='left')

        #Container que irá abrigar campo peso
        self.frame2 = Frame(self.root)
        self.frame2.pack(padx=4, pady=4)

        #Descrição e campo de entrada para o peso
        self.altura_desc = Label(self.frame2, text='Informe sua Altura', font='Arial 12 bold')
        self.altura_desc.pack(side='left')
        self.altura = Entry(self.frame2, width=5)
        self.altura.pack(side='left')

        #Botão de calculo
        self.frame3 = Frame(self.root)
        self.frame3.pack()
        self.botao = Button(self.frame3, text='Calcular', bg='blue', font='Arial 11 bold', command=self.calculaIMC)
        self.botao.pack(side='left')

        

        self.root.mainloop()

    def calculaIMC(self):
        self.peso.get(float())
        self.altura.get(float())
        self.resultado = self.peso / (self.altura ** 2)

if __name__ == '__main__':
    Imc()