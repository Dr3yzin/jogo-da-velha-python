from salvar_nome import *

class menu_orientacao:


    def historico(self):


        historico = Frame()
        historico.grid()

        ler = open('historico.txt', 'r')
        linha = ler.read()


        Label(historico, text='H I S T O R I C O', font=('Arial', 24)).grid(column=0, row=0, pady=10, padx=70)

        partidas = Label(historico, text=linha)
        partidas.grid(column=0, row=1, pady=30)

        Button(historico, text='Voltar', font=('Arial', 16), width=15, background='Yellow',
               command=lambda: [historico.destroy(), self.menu()]).grid(column=0, row=2, pady=15)



    def menu(self):
        menu = Frame(tela)
        menu.grid()
        salvar_nome = jogadores(self.menu)
        Label(menu, text='J O G O   D A   V E L H A', font=('Arial', 25)).grid(column=0, row=0, pady=10, padx=5)
        Label(menu, text='Escolha uma das opções').grid(column=0, row=1, pady=30)

        Button(menu, text='Jogar', font=('Arial', 16), width=15, background='Green',
               command=lambda: [menu.destroy(), salvar_nome.tela_player()]).grid(column=0, row=2, pady=15)

        Button(menu, text='Historico', font=('Arial', 16), width=15, background='LightBlue',
               command=lambda : [menu.destroy(), self.historico()]).grid(column=0, row=3, pady=15)

        Button(menu, text='Sair', font=('Arial', 16), width=15, background='Red', command=lambda: tela.destroy()).grid(
            column=0, row=4,
            pady=15)


if __name__ == '__main__':

    tela = Tk()
    configs = menu_orientacao()

    tela.title('Jogo da velha')
    tela.geometry('400x450+500+150')
    tela.resizable(False, False)
    tela.iconbitmap('tictac.ico')

    configs.menu()

    tela.mainloop()
