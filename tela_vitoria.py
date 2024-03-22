from tkinter import *
from PIL import Image, ImageTk

class vitoria:

    def __init__(self, vencedor, jogador1, jogador2):
        self.vencedor = vencedor
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def guardar_txt(self):
        arq = open('historico.txt', 'a')
        arq.write(self.jogador1 + ' - VS - ' + self.jogador2 + ' = ' + self.vencedor + '\n')
        arq.close()

    def vitoria(self):
        tela_vencedor = Toplevel()

        tela_vencedor.title('Jogo da velha')
        tela_vencedor.iconbitmap('tictac.ico')
        tela_vencedor.geometry('500x650+500+150')
        tela_vencedor.resizable(False, False)

        mensagem = StringVar()

        Label(tela_vencedor, textvariable=mensagem, font=('Arial', 26)).grid(column=0, row=0)

        if self.vencedor == 'Deu foi velha':
            mensagem.set(self.vencedor)
            pegar = Image.open('deu-veia.png')
            foto = pegar.resize((500, 500))
            foto = ImageTk.PhotoImage(foto)
            # foto = PhotoImage(file='deu-veia.png')

        else:
            mensagem.set(self.vencedor + ' venceu')
            pegar = Image.open('voce_ai.png')
            foto = pegar.resize((500, 500))
            foto = ImageTk.PhotoImage(foto)
            # foto = PhotoImage(file='voce_ai.png')

        Label(tela_vencedor, image=foto).grid(column=0, row=1)

        Button(tela_vencedor, text='Voltar', font=('Arial', 16), width=15, background='Green', command=lambda: tela_vencedor.destroy()).grid(column=0, row=2, pady=15)

        # Button(tela_vencedor, text='Voltar', font=('Arial', 16), width=15, background='Green',
        #        command=lambda: tela_vencedor.destroy()).grid(column=1, row=2, pady=15)

        tela_vencedor.mainloop()

if __name__ == '__main__':
    teste = vitoria('Andrey', 'Andrey', 'Sla')
    # teste = vitoria('Deu foi velha', 'Andrey', 'Sla')
    teste.guardar_txt()
    teste.vitoria()
