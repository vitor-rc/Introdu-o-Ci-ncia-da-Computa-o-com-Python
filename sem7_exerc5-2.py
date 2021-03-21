w= int(input("digite a largura: "))
h= int(input("digite a altura: "))
tab = 1
while tab <= h:
    i = 1
    while i <= w:
        if (i == w or tab == h or i==1 or tab==1):
            print("#",end="")
        else:
            print(" ",end="")
        i = i + 1
    print()
    tab = tab + 1
