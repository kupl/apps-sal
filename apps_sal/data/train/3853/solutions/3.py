def numeric_formatter(temp, numb = None):
    nb = (str(i)[-1] if not numb else numb[(i-1)%len(numb)] for i in range(1,24))
    return ''.join( e if not e.isalpha() else next(nb) for e in temp )   
