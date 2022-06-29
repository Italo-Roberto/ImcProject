from tkinter import *
from tkinter import messagebox

class Imc:
    def __init__(self):
        #Criação de janela do tkinter
        self.root = Tk()
        self.root.title('Calculadora de IMC')
        self.root.resizable(0, 0)
        self.root.geometry('320x240+500+250')

        #Container que irá abrigar campo peso
        self.frame1 = Frame(self.root)
        self.frame1.pack(padx=5, pady=5)

        #Descrição e campo de entrada para o peso
        self.peso_desc = Label(self.frame1, text='Informe seu peso', font='Arial 12 bold')
        self.peso_desc.pack(side='left')
        self.peso = Entry(self.frame1, width=5)
        self.peso.pack(side='left', padx=5, pady=5)

        #Container que irá abrigar campo peso
        self.frame2 = Frame(self.root)
        self.frame2.pack(padx=5, pady=5)

        #Descrição e campo de entrada para o peso
        self.altura_desc = Label(self.frame2, text='Informe sua Altura', font='Arial 12 bold')
        self.altura_desc.pack(side='left')
        self.altura = Entry(self.frame2, width=5)
        self.altura.pack(side='left', padx=5, pady=5)

        #Botão de calculo
        self.frame3 = Frame(self.root)
        self.frame3.pack()
        self.botao = Button(self.frame3, text='Calcular', bg='blue', fg='white', font='Arial 11 bold', command=self.calculaIMC)
        self.botao.pack(side='left')

        self.root.mainloop()

    def calculaIMC(self):
        pes = float(self.peso.get())
        alt = float(self.altura.get())
        self.resultado = pes / (alt ** 2)

        if self.resultado < 18.5:
            messagebox.showwarning(title="Você está abaixo do peso!", message=f'Seu imc é: {float(self.resultado)}')
        elif self.resultado > 18.5 and self.resultado <= 24.9:
            messagebox.showinfo(title="Ok, seu peso é o ideal", message=f'Seu imc é: {float(self.resultado)}')
        elif self.resultado > 25 and self.resultado <= 29.9:
            messagebox.showwarning(title="Atenção! Você está com sobrepeso", message=f'Seu imc é: {float(self.resultado)}')
        elif self.resultado > 30 and self.resultado <= 34.9:
            messagebox.showerror(title="Cuidado! Você está com Obesidade GRAU 1!", message=f'Seu imc é: {float(self.resultado)}')
        else:
            messagebox.showerror(title="Cuidado! VocÊ está com obesidade GRAU 2!", message=f'Seu imc é: {float(self.resultado)}')

if __name__ == '__main__':
    Imc()