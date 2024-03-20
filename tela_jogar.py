from tkinter import *
from verificacoes import *


# texto = StringVar()

class jogar:

    def __init__(self):
        self.velha = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.round = 0


    def trocar_sinal(self):
        if self.round % 2 == 0:
            return 'O'

        return 'X'

    def marcar(self, a, b, x):
        self.round += 1
        self.velha[a][b] = self.trocar_sinal()

        # print(self.velha)

        match x:
            case 1:
                self.sinal1.set(self.velha[a][b])

            case 2:
                self.sinal2.set(self.velha[a][b])

            case 3:
                self.sinal3.set(self.velha[a][b])

            case 4:
                self.sinal4.set(self.velha[a][b])

            case 5:
                self.sinal5.set(self.velha[a][b])

            case 6:
                self.sinal6.set(self.velha[a][b])

            case 7:
                self.sinal7.set(self.velha[a][b])

            case 8:
                self.sinal8.set(self.velha[a][b])

            case 9:
                self.sinal9.set(self.velha[a][b])

        if verificar(self.velha) == 'X':
            print('X venceu')

        elif verificar(self.velha) == 'O':
            print('O venceu')

        elif self.round >= 9:
            print('Deu foi velha ó')
            for a in range(3):
                for b in range(3):
                    self.velha[a][b] = self.round
                    self.round -= 1
            print(self.velha)
            self.round = 0




    def declarando_dinamismo(self):
        self.sinal1 = StringVar()
        self.sinal2 = StringVar()
        self.sinal3 = StringVar()
        self.sinal4 = StringVar()
        self.sinal5 = StringVar()
        self.sinal6 = StringVar()
        self.sinal7 = StringVar()
        self.sinal8 = StringVar()
        self.sinal9 = StringVar()


    def tela_jogar(self):
        texto = []
        botao = []
        tela_jogar = Toplevel()

        tela_jogar.title('Jogo da velha')
        tela_jogar.iconbitmap('tictac.ico')
        tela_jogar.geometry('400x450+500+150')
        tela_jogar.resizable(False, False)

        self.declarando_dinamismo()

        # Label(tela_jogar, text='T E X T O   T E S T E', font=('Arial', 26)).grid(column=0, row=0, pady=30, padx=25)
        Label(tela_jogar, text='', font=('Arial', 26)).grid(column=0, row=0, pady=10)

        Label(tela_jogar, text='', font=('Arial', 26)).grid(column=0, row=1, padx=20)

        texto1 = Label(tela_jogar, font=('Arial', 60), textvariable=self.sinal1)
        texto1.grid(column=1, row=1, padx=21)
        botao1 = Button(tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(0, 0, 1), botao1.destroy()])
        botao1.grid(column=1, row=1, padx=15)

        texto2 = Label(tela_jogar, font=('Arial', 60), textvariable=self.sinal2)
        texto2.grid(column=2, row=1, padx=15)
        botao2 = Button(tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(0, 1, 2), botao2.destroy()])
        botao2.grid(column=2, row=1, padx=15)

        texto3 = Label(tela_jogar, font=('Arial', 60), textvariable=self.sinal3)
        texto3.grid(column=3, row=1, padx=15)
        botao3 = Button(tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(0, 2, 3), botao3.destroy()])
        botao3.grid(column=3, row=1, padx=15)

        Label(tela_jogar, text='', font=('Arial', 26)).grid(column=0, row=2, padx=20, pady=50)

        texto4 = Label(tela_jogar, font=('Arial', 60), textvariable=self.sinal4)
        texto4.grid(column=1, row=2, padx=15)
        botao4 = Button(tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(1, 0, 4), botao4.destroy()])
        botao4.grid(column=1, row=2, padx=15)

        texto5 = Label(tela_jogar, font=('Arial', 60), textvariable=self.sinal5)
        texto5.grid(column=2, row=2, padx=15)
        botao5 = Button(tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(1, 1, 5), botao5.destroy()])
        botao5.grid(column=2, row=2, padx=15)

        texto6 = Label(tela_jogar, font=('Arial', 60), textvariable=self.sinal6)
        texto6.grid(column=3, row=2, padx=15)
        botao6 = Button(tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(1, 2, 6), botao6.destroy()])
        botao6.grid(column=3, row=2, padx=15)

        Label(tela_jogar, text='', font=('Arial', 26)).grid(column=0, row=3, padx=20)

        texto7 = Label(tela_jogar, font=('Arial', 60), textvariable=self.sinal7)
        texto7.grid(column=1, row=3, padx=15)
        botao7 = Button(tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(2, 0, 7), botao7.destroy()])
        botao7.grid(column=1, row=3, padx=15)

        texto8 = Label(tela_jogar, font=('Arial', 60), textvariable=self.sinal8)
        texto8.grid(column=2, row=3, padx=15)
        botao8 = Button(tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(2, 1, 8), botao8.destroy()])
        botao8.grid(column=2, row=3, padx=15)

        texto9 = Label(tela_jogar, font=('Arial', 60), textvariable=self.sinal9)
        texto9.grid(column=3, row=3, padx=15)
        botao9 = Button(tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(2, 2, 9), botao9.destroy()])
        botao9.grid(column=3, row=3, padx=15)

        tela_jogar.mainloop()



if __name__ == '__main__':
    sla = jogar()
    sla.tela_jogar()
