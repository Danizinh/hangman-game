from random import choice
print('-=-'* 20)
print("WELCOME TO FORCA")
print('-=-'* 20)
with open("palavras.txt")as arquivo:
    linhas = arquivo.read()
    listas_de_palavras = linhas.split('\n')

secreto = choice(listas_de_palavras).upper()

digitadas = []
chances = 10

while True:
    if chances <= 0:
        print("VOCE PERDEUUUUUUUUUUUUUUUUUUUUUUUUUUUU ")
        break

    letra = input("Digite uma letra:").upper()

    if len(letra) > 1:
        print("Ahhhhh isso nao vale, digite  apenas um letra")
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'UHUULLLLLL, A LETRA "{letra}"EXISTE NA PALAVRA SECRETA..')
    else:
        print(f'AFFzzzz: A LETRA "{letra}"NAO EXISTE NA PALAVRA SECRETA......')
        digitadas.pop()
    print(digitadas)

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(
            f'VOCÊ GANHOOUUUUUUUUUUUUUUU!!! A palavra era {secreto_temporario}.')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

        if letra not in secreto_temporario:
            chances = chances - 1
    print(f"Voce ainda tem {chances} CHANCES.")
    print()
