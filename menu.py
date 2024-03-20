# import tkinter
from tkinter import ttk
from tela_jogar import *


def config(x):
    print(x)
    configurar = Toplevel(menu1)

    configurar.title('Jogo da velha')
    configurar.geometry('400x450')
    configurar.resizable(False, False)
    configurar.iconbitmap('tictac.ico')

    lista = ['valor1', 'valor2', 'valor3']

    Label(configurar, text='C O N F I G U R A Ç Õ E S', font=('Arial', 24)).grid(column=0, row=0, pady=10, padx=4)

    combo = ttk.Combobox(configurar, values=lista)
    combo.grid(column=0, row=1, pady=30)

    Button(configurar, text='Voltar', font=('Arial', 16), width=15, background='Yellow',
           command=configurar.destroy).grid(column=0, row=2, pady=15)

    configurar.mainloop()


def sair():
    menu1.destroy()


if __name__ == '__main__':

    jogo = jogar()
    menu1 = Tk()

    menu1.title('Jogo da velha')
    menu1.geometry('400x450+500+150')
    menu1.resizable(False, False)
    menu1.iconbitmap('tictac.ico')

    Label(menu1, text='J O G O   D A   V E L H A', font=('Arial', 25)).grid(column=0, row=0, pady=10, padx=5)
    Label(menu1, text='Escolha uma das opções').grid(column=0, row=1, pady=30)

    Button(menu1, text='Jogar', font=('Arial', 16), width=15, background='Green', command=jogo.tela_jogar).grid(column=0,
                                                                                                           row=2,
                                                                                                           pady=15)

    Button(menu1, text='Configurações', font=('Arial', 16), width=15, background='LightBlue', command=lambda: config(23)).grid(column=0, row=3, pady=15)


    Button(menu1, text='Sair', font=('Arial', 16), width=15, background='Red', command=sair).grid(column=0, row=4,
                                                                                                  pady=15)

    menu1.mainloop()
