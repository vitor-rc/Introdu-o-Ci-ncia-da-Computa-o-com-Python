def computador_escolhe_jogada(n,m):
    p = 1
    while (p < m):
        if ((n-p)%(m+1)==0):
            return p
        else:
            p+=1
    return p

def usuario_escolhe_jogada(n,m):
    valido = 0
    while (valido == 0): 
        p = int(input("Quantas peças você vai tirar? "))
        if (p>0 and p <= m and p<=n):
            valido = 1
        else:
            print("Oops! Jogada inválida! Tente de novo.")
            valido = 0
    return p

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    pecas = n
    if(n%(m+1)!=0):
        print("Computador começa!")
        p = computador_escolhe_jogada(n,m)
        pecas = pecas - p
        print("O computador tirou",p,"peça(s).")
        print("Agora restam",pecas,"peças no tabuleiro.")
    else:
        print("Voce começa!")
    
    while (pecas >0):
        p = usuario_escolhe_jogada(pecas,m)
        pecas = pecas - p
        print("Você tirou",p,"peça(s).")
        if (pecas ==0):
                print("Fim do jogo! Você ganhou!")
                return 0
        print("Agora restam",pecas,"peças no tabuleiro.")
        p = computador_escolhe_jogada(pecas,m)
        pecas = pecas - p
        print("O computador tirou",p,"peça(s).")
        print("Agora restam",pecas,"peças no tabuleiro.")
        if (pecas ==0):
                print("Fim do jogo! O computador ganhou!")
                return 1

def campeonato():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    tipo = int(input())
    plac_comp = 0
    plac_voce = 0
    if(tipo == 2):
        print("Voce escolheu um campeonato!")
        for i in range(3):
            print("**** Rodada", i+1,"****")
            g = partida()
            if g:
                plac_comp+=1
            else:
                plac_voce+=1
        print("**** Final do campeonato! ****")
        print("Placar: Você",plac_voce,"X",plac_comp,"Computador")
    else:
        print("Voce escolheu uma partida isolada!")
        partida()

campeonato()
#usuario_escolhe_jogada(5,3)
