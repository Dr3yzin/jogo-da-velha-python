from tela_jogar import *


class jogadores:

    def __init__(self):
        self.p1 = None
        self.p2 = None

    def destruir(self):
        self.pegar_players.destroy()

    def definir_nomes(self, x, y):
        if x == '' or x[0] == ' ':
            self.p1 = 'Player 1'
        else:
            self.p1 = x
        if y == '' or y[0] == ' ' or x == y:
            self.p2 = 'Player 2'
        else:
            self.p2 = y

    def tela_player(self):
        self.pegar_players = Toplevel()

        self.pegar_players.title('Jogo da velha')
        self.pegar_players.iconbitmap('tictac.ico')
        self.pegar_players.geometry('400x450+500+150')
        self.pegar_players.resizable(False, False)

        Label(self.pegar_players, text='P L A Y E R S', font=('Arial', 25)).grid(column=0, row=0, pady=50, padx=90)

        Label(self.pegar_players, text='Defina o nome do player 1:').grid(column=0, row=1, pady=10)
        player1 = Entry(self.pegar_players, background='LightBlue', width=40)
        player1.grid(column=0, row=2)


        Label(self.pegar_players, pady=10).grid(column=0, row=3)

        Label(self.pegar_players, text='Defina o nome do player 2:').grid(column=0, row=4, pady=10)
        player2 = Entry(self.pegar_players, background='LightBlue', width=40)
        player2.grid(column=0, row=5)


        Button(self.pegar_players, text='Iniciar', font=('Arial', 16), width=15, background='Green', command=lambda: [self.definir_nomes(player1.get(), player2.get()), jogar(self.p1, self.p2, self.pegar_players).jogar()]).grid(column=0, row=6, pady=55)

        self.pegar_players.mainloop()

