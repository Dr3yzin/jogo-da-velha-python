from tela_jogar import *


class jogadores:

    def __init__(self, menu):
        self.p1 = 'Player 1'
        self.p2 = 'Player 2'
        self.menu = menu

    def definir_nomes(self, x, y):
        if x != '' and x[0] != ' ':
            self.p1 = x

        if y != '' and y[0] != ' ' and x != y:
            self.p2 = y

    def iniciar(self, nome1, nome2):
        self.definir_nomes(nome1, nome2)
        jogue = jogar(self.p1, self.p2, self.pegar_players, self.menu)
        self.pegar_players.destroy(), jogue.jogar()

    def tela_player(self):
        self.pegar_players = Frame()
        self.pegar_players.grid()

        Label(self.pegar_players, text='P L A Y E R S', font=('Arial', 25)).grid(column=0, row=0, pady=50, padx=90)

        Label(self.pegar_players, text='Defina o nome do player 1:').grid(column=0, row=1, pady=10)
        player1 = Entry(self.pegar_players, background='LightBlue', width=40)
        player1.grid(column=0, row=2)


        Label(self.pegar_players, pady=10).grid(column=0, row=3)

        Label(self.pegar_players, text='Defina o nome do player 2:').grid(column=0, row=4, pady=10)
        player2 = Entry(self.pegar_players, background='LightBlue', width=40)
        player2.grid(column=0, row=5)


        Button(self.pegar_players, text='Iniciar', font=('Arial', 16), width=15, background='Green', command=lambda: [self.iniciar(player1.get(), player2.get())]).grid(column=0, row=6, pady=55)


