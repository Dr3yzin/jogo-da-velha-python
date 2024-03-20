from tkinter import *

def printar(x, y):
    print(x)
    print(y)

def tela_player():
    pegar_players = Toplevel()

    pegar_players.title('Jogo da velha')
    pegar_players.iconbitmap('tictac.ico')
    pegar_players.geometry('400x450+500+150')
    pegar_players.resizable(False, False)

    Label(pegar_players, text='P L A Y E R S', font=('Arial', 25)).grid(column=0, row=0, pady=50, padx=90)

    Label(pegar_players, text='Defina o nome do player 1:').grid(column=0, row=1, pady=10)
    player1 = Entry(pegar_players, background='LightBlue', width=40)
    player1.grid(column=0, row=2)

    p1 = player1.get()

    Label(pegar_players, pady=10).grid(column=0, row=3)

    Label(pegar_players, text='Defina o nome do player 2:').grid(column=0, row=4, pady=10)
    player2 = Entry(pegar_players, background='LightBlue', width=40)
    player2.grid(column=0, row=5)

    p2 = player2.get()

    Button(pegar_players, text='Iniciar', font=('Arial', 16), width=15, background='Green', command=lambda: printar(p1, p2)).grid(column=0, row=6, pady=55)

    pegar_players.mainloop()


if __name__ == '__main__':
    tela_player()