def array(string):
    liste=string.split(',')
    if len(liste)>2:
        liste.pop()
        return ' '.join(liste[1:])

