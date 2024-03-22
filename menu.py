from salvar_nome import *

class menu_orientacao:

    def __init__(self):
        self.apenas_uma = 0

    def historico(self):
        if self.apenas_uma == 1:
            pass
        else:
            self.apenas_uma += 1
            historico = Frame(menu)
            historico.grid()

            ler = open('historico.txt', 'r')
            linha = ler.read()

            # historico.title('Jogo da velha')
            # historico.geometry('400x450')
            # historico.resizable(False, False)
            # historico.iconbitmap('tictac.ico')

            historico.grid_rowconfigure(0, weight=1)
            historico.grid_columnconfigure(0, weight=1)

            # Label(historico, text='H I S T O R I C O', font=('Arial', 24)).grid(column=0, row=0, pady=10, padx=4)
            Label(historico, text='H I S T O R I C O', font=('Arial', 24)).place(x=10, y=10)

            partidas = Label(historico, text=linha)
            partidas.grid(column=0, row=1, pady=30, sticky=EW)

            Button(historico, text='Voltar', font=('Arial', 16), width=15, background='Yellow',
                   command=lambda: [historico.destroy(), self.__init__()]).grid(column=0, row=2, pady=15)

            # scroll = ttk.Scrollbar(historico, orient='vertical', command=partidas.yview)
            # scroll.grid(column=1, row=0, sticky=NS)

            # partidas['yscrollcommand'] = scroll.set

            historico.mainloop()

    def menu(self):
        print('a')


if __name__ == '__main__':

    menu = Tk()
    salvar_nome = jogadores()
    configs = menu_orientacao()

    menu.title('Jogo da velha')
    menu.geometry('400x850+500+150')
    menu.resizable(False, False)
    menu.iconbitmap('tictac.ico')

    Label(menu, text='J O G O   D A   V E L H A', font=('Arial', 25)).grid(column=0, row=0, pady=10, padx=5)
    Label(menu, text='Escolha uma das opções').grid(column=0, row=1, pady=30)

    Button(menu, text='Jogar', font=('Arial', 16), width=15, background='Green', command=salvar_nome.tela_player).grid(column=0,
                                                                                                                       row=2,
                                                                                                                       pady=15)

    Button(menu, text='Historico', font=('Arial', 16), width=15, background='LightBlue', command=configs.historico).grid(column=0, row=3, pady=15)


    # Button(menu, text='Sair', font=('Arial', 16), width=15, background='Red', command=lambda: menu.destroy()).grid(column=0, row=4,
    #                                                                                              pady=15)
    Button(menu, text='Sair', font=('Arial', 16), width=15, background='Red', command=lambda: menu.destroy()).place(x=12, y=20)

    menu.mainloop()
