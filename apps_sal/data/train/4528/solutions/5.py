
def my_languages(results):
    lista=[]
    for i in results:
        if results[i]>=60 and i not in lista:
            lista.append(results[i])
    
     
    lista.sort()
    lista2=[]
    for i in lista:
        for c in results:
            if i==results[c]:
                lista2.append(c)
    lista2=lista2[::-1]
            
    
    return lista2
