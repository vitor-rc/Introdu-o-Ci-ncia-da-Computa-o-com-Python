def remove_repetidos(lista):
    nova = []
    for item in lista:
        vai_entrar = 1
        for novo in nova:
            if item == novo:
                vai_entrar = 0
        if vai_entrar:
            nova.append(item)
    nova.sort()
    return nova
