def c(lista):
    x = lambda a:(a,lista.count(a))
    return x
def star(n):
    s = ''
    for i in range(n):
        s = s +'*'
    return s
        
def remover(lista):
    l = []
    for i in lista:
        if i in l : continue
        l.append(i)
    return l 
def get_strings(city):
    letters = remover(list((city.lower())))
    huss = list(map(c(city.lower()) , letters))
    
    s = ''
    for letter,co in huss:
        if letter == ' ': continue
        s = s + letter + ':'+star(co)+',' 
        s = s.strip()
    return s[:-1]
    

