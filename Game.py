from time import sleep

from Palavras import *
from Telas import *
from Forca import *


t = Telas()
Telas.inicial(t)
jogar = t.get_jogar()

while jogar:

    os.system("clear")

    # Contagem de erros para renderizar a forca correspondente
    erros = 0

    # Instanciação do objeto Forca
    f = Forca()
    # Carregando banco de dado de palavras
    p = Palavras(f"BancoDePalavras/{t.get_arquivo_level()}")

    # Fazendo uma cópia da palavra escolhida para outro dicionário para transformar em simbolo para usar como referência
    copy_palavra = {}

    # Pegando o dicionário e transformando em uma palavra sem espaços
    palavra = ""

    # Pegando a palavra escolhida e transformando em símbolo sem espaços
    caracteres = ""

    # Contagem de keys para transformar o copyPalavra em dicionário
    n = 0

    # Transformando os caracteres no símbolo _
    for i in p.escolha().values():
        copy_palavra[f"{n}"] = "_ "
        palavra += i
        n += 1
        print(n)

    # Medindo tamanho da palavra para ver quando venceu
    g = len(palavra)

    # Varrendo o dicionário copyPalavra para transformar em símbolo sem espaços
    for o in copy_palavra.values():
        c = copy_palavra.copy().values()
        for i in c:
            caracteres += i + " "
        break

    # Lista de letras certas
    certas = ""
    # Lista de letras erradas
    erradas = ""

    # Loop do jogo
    loop = True
    while loop:

        # Renderizar nome do jogo, forca e qual a palavra
        Palavras.clear()

        f.forcas(erros)
        print(f"Palavra ({len(palavra)} letras): {caracteres}")

        # Renderização de letras certas
        if len(certas) > 0:
            print(f"\nLetras certas: {certas}")
        else:
            print("\nLetras certas: nenhuma")

        # Renderização de letras erradas
        if len(erradas) > 0:
            print(f"Letras erradas: {erradas}\n")
        else:
            print("Letras erradas: nenhuma\n")

        # Digitando uma letra
        letra = input("Digite uma letra: ")

        # Validando se o input é uma letra e apenas uma letra
        if len(letra) == 1 and letra.isalpha():

            # Verificação de letra na palavra
            if palavra.count(letra) > 0:

                caracteres = ""
                op = 0

                for y in palavra:
                    if y.count(letra) == 1 and certas.count(letra) == 0:
                        copy_palavra.update({f"{op}": f"{letra}"})
                        g -= 1
                    op += 1

                for o in copy_palavra.values():
                    c = copy_palavra.copy().values()
                    for i in c:
                        caracteres += i
                    break

                if certas.count(letra) == 0:
                    certas += f"{letra}, "

                if g <= 0:
                    loop = False

            else:
                if erradas.count(letra) == 0:
                    erradas += f"{letra}, "
                    erros += 1

                if erros == 7:
                    loop = False

        print(f"Palavra: {caracteres}")

    # FIM DE JOGO
    t_f = Telas(palavra, certas, erradas, erros)

    if g == 0:
        t_f.tela_final("Parabéns você ganhou :D")

    if erros == 7:
        t_f.tela_final("Infelizmente você perdeu :C")

    sleep(2)

    Palavras.clear()

    r = input("\nDeseja ir para a tela inicial ou encerrar o jogo ?\n\n1 - Tela Inicial\n2 - Sair\n\nResposta: ")

    if int(r) == 1:
        # jogar = False
        Telas.inicial(t)
        jogar = True
    if int(r) == 2:
        jogar = False
        os.system("exit")

else:
    Palavras.clear()
    print("\nAgradecemos muito por ter jogado o nosso jogo!\n\nVolte sempre :D\n")
    sleep(2)
    os.system("exit")
    os.system("clear")
