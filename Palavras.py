import random
from Telas import *

t = Telas()


class Palavras:

    def __init__(self, path=None):
        if path is None:
            self.path = path
        else:
            self.path = path + ".txt"

    def escolha(self):
        """
        :param self: Caminho do arquivo de texto.
        :return: Retornará um dicionário com palavra escolhida dentro das que estão dentro do arquivo.
        """
        palavras_arquivo = []
        palavra_escolhida = {}
        k = 0

        arq = open(self.path, "r")

        for p in arq.read().split("\n"):
            p.strip(" ")
            palavras_arquivo.append(p)

        escolhida = random.choice(palavras_arquivo)

        for i in escolhida:
            palavra_escolhida[f"{k}"] = i
            k += 1

        return palavra_escolhida

    @staticmethod
    def gravar():
        Palavras.clear()

        print("\nEm qual nível deseja gravar a nova palavra ?\n")

        lista = t.listar_diretorios()

        g = input("\nResposta: ")

        arquivo = open(f"{t.banco_palavras}/{lista[int(g) - 1]}", "a")

        cadastrar = True

        while cadastrar:

            p = input("\nDigite uma palavra: ")
            novas_palavras = list()

            for novas in p.split(" "):
                novas = novas.strip(" ")
                novas = novas.rstrip("\n")
                novas = novas.lstrip("\n")
                novas = novas.rstrip(",")
                novas = novas.lstrip(",")
                novas = novas.rstrip()
                novas = novas.lstrip()

                novas_palavras.append(f"\n{novas.lower()}")

            palavras.Palavras().clear()

            escolha = input(
                "\nDeseja cadastrar mais alguma palavra ?\n\n1 - Sim\n2 - Não\n3 - Cancelar Edição\n\nResposta: ")

            if int(escolha) == 1:
                cadastrar = True
            elif int(escolha) == 2:
                cadastrar = False
                arquivo.writelines(novas_palavras)
            elif int(escolha) == 3:
                cadastrar = False

        arquivo.close()

        Palavras.clear()
        r = input("\nDeseja jogar ou encerrar o jogo ?\n\n1 - Jogar\n2 - Sair\n\nResposta: ")

        if int(r) == 1:
            t.escolher_level()
        if int(r) == 2:
            os.system("exit")

    @staticmethod
    def clear():
        os.system("clear")
        print(t.nome_jogo)
