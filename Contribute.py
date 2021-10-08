def remove_duplcates(lista):
    lista2=[]
    for item in lista:
        if item not in lista2:
           lista2.append(item)
    return lista2
