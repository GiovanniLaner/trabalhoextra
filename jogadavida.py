from itertools import count
import random


jogadorUm = input('Informe o nome do jogador 1:')
jogadorDois = input('Informe o nome do jogador 2:')




def rodarDados(rodarDado, numeroCasa):
    numeroCasa = 0
    rodarDado = print('Ande', random.randint(1, 6), 'casa(as)') #sorteia o numero do dado
    numeroCasa = numeroCasa + rodarDado
    return rodarDado, numeroCasa

def executaRegras(numeroCasa):
        if numeroCasa == 1 or numeroCasa == 3 or numeroCasa == 10 or numeroCasa == 17:
            dadoCasa()
        elif numeroCasa == 2 or numeroCasa == 8 or numeroCasa == 18:
            morreCasa()
        elif numeroCasa == 4 or numeroCasa == 11 or numeroCasa == 19:
            desafioMatematicoCasa()
        elif numeroCasa == 5:
            formaturaCasa()
        elif numeroCasa == 6 or numeroCasa == 9 or numeroCasa == 13:
            terFilhosCasa()
        elif numeroCasa == 7:
            casarCasa()
        elif numeroCasa == 12:
            divorciarCasa()
        elif numeroCasa == 14:
            loteriaCasa()
        elif numeroCasa == 15:
            ficarFamosoCasa()
        elif numeroCasa == 16:
            casarNovamenteCasa()
        elif numeroCasa == 20:
            voltarCasas()   
        return numeroCasa

def dadoCasa(numeroCasa):
        
        jogarNovamente = random.randint(1, 6)

        if jogarNovamente == 1:
            numeroCasa = numeroCasa + 1
            print('Avance uma casa.')
        elif jogarNovamente == 3:
            numeroCasa = numeroCasa - 1
            print('Volte uma casa.')
        elif jogarNovamente == 6:
            numeroCasa = numeroCasa - numeroCasa
            print('Você perdeu, volte ao inicio.')    
        else:
            print('O jogo quebrou kk')
        return jogarNovamente, numeroCasa

def morreCasa(numeroJogador):
    

    print('Você morreu, volte ao começo', numeroJogador)

    return numeroJogador

def desafioMatematicoCasa(numeroJogador):

    return numeroJogador

def formaturaCasa(numeroJogador):
    print('Você se formou, rode o dado novamente e veja em qual curso foi.')
    
    if rodarDados() == 1:
        print('Formou-se em Direto!')
    elif rodarDados() == 2:
        print('Formou-se em Gastronomia!')
    elif rodarDados() == 3:
        print('Formou-se em Engenharia Civil!')
    elif rodarDados() == 4:
        print('Formou-se em Educação Física!')
    elif rodarDados() == 5:
        print('Formou-se em Astronomia!')
    elif rodarDados() == 6:
        print('Formou-se em Música!')
    else:
        print('Jogo quebrou novamente kk.')    

    return numeroJogador

def terFilhosCasa(numeroJogador):
    filho = 0

    if rodarDados() == 5:
        filho = filho + 2
        print('Você teve gêmeos, desepesas em dobro! kkk')
    else:
        filho = filho + 1
        print('Você foi premiado com um bebê!')

    return numeroJogador

def casarCasa(numeroJogador):
    casamento = False
    
    if numeroJogador == True:
        casamento == True
        return True
    else:
        print('Jogou quebrou de novo XD')

    return numeroJogador

def ficarFamosoCasa(numeroJogador):

    return numeroJogador

def divorciarCasa(numeroJogador):

    return numeroJogador

def loteriaCasa(numeroJogador):
    
    return numeroJogador

def casarNovamenteCasa(numeroJogador):

    return numeroJogador

def voltarCasas(numeroJogador):

    return numeroJogador

executaRegras()
