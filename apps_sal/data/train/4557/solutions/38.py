def row_weights(array):
    lista = []
    lista2 = []
    for i in range(0,len(array),2):
        lista.append(array[i])
    for i in range(1,len(array),2):
        lista2.append(array[i])
    convert = sum(i for i in lista)
    convert2 = sum(i for i in lista2)
    return ((convert, convert2))
    
    
    

   
   
    

