from verificacoes import *
from tela_vitoria import *
class jogar:

    def __init__(self, player1, player2, pegar_player, menu):
        self.player1 = player1
        self.player2 = player2
        self.velha = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.round = 0
        self.pegar_player = pegar_player
        self.menu = menu

    def redefinir(self):
        aux = 1
        for a in range(3):
            for b in range(3):
                self.velha[a][b] = aux
                aux += 1
        self.round = 0

    def trocar_sinal(self):
        if self.round % 2 == 0:
            return 'O'

        return 'X'


    def marcar(self, a, b, x):
        self.round += 1
        self.velha[a][b] = self.trocar_sinal()


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



    def verificar_acabou(self):

        if verificar(self.velha) == 'X':
            self.redefinir()
            aux = vitoria(self.player1, self.player1, self.player2)
            aux.guardar_txt()
            self.tela_jogar.destroy()
            self.menu()
            aux.vitoria()



        elif verificar(self.velha) == 'O':
            self.redefinir()
            aux = vitoria(self.player2, self.player1, self.player2)
            aux.guardar_txt()
            self.tela_jogar.destroy()
            self.menu()
            aux.vitoria()


        elif self.round >= 9:
            self.redefinir()
            aux = vitoria('Deu foi velha', self.player1, self.player2)
            aux.guardar_txt()
            self.tela_jogar.destroy()
            self.menu()
            aux.vitoria()





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


    def jogar(self):
        self.tela_jogar = Frame()
        self.tela_jogar.grid()

        self.declarando_dinamismo()

        # Label(tela_jogar, text='T E X T O   T E S T E', font=('Arial', 26)).grid(column=0, row=0, pady=30, padx=25)
        Label(self.tela_jogar, text='', font=('Arial', 26)).grid(column=0, row=0, pady=10)

        Label(self.tela_jogar, text='', font=('Arial', 26)).grid(column=0, row=1, padx=20)



        texto1 = Label(self.tela_jogar, font=('Arial', 60), textvariable=self.sinal1)
        texto1.grid(column=1, row=1, padx=21)

        botao1 = Button(self.tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(0, 0, 1), botao1.destroy(), self.verificar_acabou()])
        botao1.grid(column=1, row=1, padx=15)



        texto2 = Label(self.tela_jogar, font=('Arial', 60), textvariable=self.sinal2)
        texto2.grid(column=2, row=1, padx=15)

        botao2 = Button(self.tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(0, 1, 2), botao2.destroy(), self.verificar_acabou()])
        botao2.grid(column=2, row=1, padx=15)



        texto3 = Label(self.tela_jogar, font=('Arial', 60), textvariable=self.sinal3)
        texto3.grid(column=3, row=1, padx=15)

        botao3 = Button(self.tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(0, 2, 3), botao3.destroy(), self.verificar_acabou()])
        botao3.grid(column=3, row=1, padx=15)



        Label(self.tela_jogar, text='', font=('Arial', 26)).grid(column=0, row=2, padx=20, pady=50)



        texto4 = Label(self.tela_jogar, font=('Arial', 60), textvariable=self.sinal4)
        texto4.grid(column=1, row=2, padx=15)

        botao4 = Button(self.tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(1, 0, 4), botao4.destroy(), self.verificar_acabou()])
        botao4.grid(column=1, row=2, padx=15)



        texto5 = Label(self.tela_jogar, font=('Arial', 60), textvariable=self.sinal5)
        texto5.grid(column=2, row=2, padx=15)

        botao5 = Button(self.tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(1, 1, 5), botao5.destroy(), self.verificar_acabou()])
        botao5.grid(column=2, row=2, padx=15)



        texto6 = Label(self.tela_jogar, font=('Arial', 60), textvariable=self.sinal6)
        texto6.grid(column=3, row=2, padx=15)

        botao6 = Button(self.tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(1, 2, 6), botao6.destroy(), self.verificar_acabou()])
        botao6.grid(column=3, row=2, padx=15)



        Label(self.tela_jogar, text='', font=('Arial', 26)).grid(column=0, row=3, padx=20)



        texto7 = Label(self.tela_jogar, font=('Arial', 60), textvariable=self.sinal7)
        texto7.grid(column=1, row=3, padx=15)

        botao7 = Button(self.tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(2, 0, 7), botao7.destroy(), self.verificar_acabou()])
        botao7.grid(column=1, row=3, padx=15)



        texto8 = Label(self.tela_jogar, font=('Arial', 60), textvariable=self.sinal8)
        texto8.grid(column=2, row=3, padx=15)

        botao8 = Button(self.tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(2, 1, 8), botao8.destroy(), self.verificar_acabou()])
        botao8.grid(column=2, row=3, padx=15)



        texto9 = Label(self.tela_jogar, font=('Arial', 60), textvariable=self.sinal9)
        texto9.grid(column=3, row=3, padx=15)

        botao9 = Button(self.tela_jogar, width=9, height=4, background='Black',
                        command=lambda: [self.marcar(2, 2, 9), botao9.destroy(), self.verificar_acabou()])
        botao9.grid(column=3, row=3, padx=15)



