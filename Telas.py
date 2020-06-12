import os
from time import sleep

import Palavras as palavras
from Forca import *

f = Forca()


class Telas:
    
    nome_jogo = ">>>>>> Jogo da Forca <<<<<<"
    level = 1
    banco_palavras = "BancoDePalavras"
    arquivo_level = []
    jogar = False

    def __init__(self, palavra=None, certas=None, erradas=None, erros=None):
        self.palavra = palavra
        self.certas = certas
        self.erradas = erradas
        self.erros = erros

    def get_level(self):
        return self.level

    def get_jogar(self):
        return self.jogar

    @staticmethod
    def get_arquivo_level():
        if len(Telas.arquivo_level) == 0:
            Telas.arquivo_level = "facil"
        return Telas.arquivo_level

    def inicial(self):

        palavras.Palavras().clear()

        if not self.jogar:
            e = input("\nDeseja gravar novas palavras para jogar com seus amigos\nou prefere jogar com o banco de "
                      "palavras que já tem ?\n\n1 - Jogar\n2 - Gravar\n3 - Sair\n\nResposta: ")
        else:
            e = input("\nDeseja gravar novas palavras para jogar com seus amigos\nou prefere jogar com o banco de "
                      "palavras que já tem ?\n\n1 - Jogar\n2 - Gravar\n\nResposta: ")

        if int(e) == 1:
            self.jogar = True
            Telas.escolher_level()
        elif int(e) == 2:
            p = palavras.Palavras()
            p.gravar()
        elif int(e) == 3:
            os.system("exit")

    @staticmethod
    def escolher_level():

        palavras.Palavras().clear()

        arquivos = Telas.listar_diretorios()
        a_p = Telas.get_arquivo_level()

        level = input("\nEscolha o seu level: ")

        # Se o usuário digitar uma letra
        while level.isalpha() or int(level) > len(arquivos):

            arquivos = Telas.listar_diretorios()

            level = input("\nEscolha o seu level: ")

        Telas.arquivo_level = a_p[int(level) - 1]
        Telas.jogar = True

    def tela_final(self, mensagem):

        palavras.Palavras().clear()

        f.forcas(self.erros)
        print(f"\n>>>>>>>>>>>> {mensagem} <<<<<<<<<<<<")
        print(f"\nA palavra certa: {self.palavra}")
        print(f"\nLetras certas: {self.certas}")
        print(f"Letras erradas: {self.erradas}\n")
        sleep(20)

    @staticmethod
    def listar_diretorios():

        arquivos = os.listdir(Telas.banco_palavras)
        arq = os.scandir(Telas.banco_palavras)
        arquivos_palavras = []

        i = 1

        for d in arq:
            d = d.name.split('.')[0]
            print(f"{i} - {d.capitalize()}")
            arquivos_palavras.append(d)
            i += 1
            
        Telas.arquivo_level = arquivos_palavras

        return arquivos
