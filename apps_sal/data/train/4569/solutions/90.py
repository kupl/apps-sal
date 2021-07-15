def next_item(xs, item):
    if type(xs) == str or type(xs) == list:
        if item not in xs or item == xs[-1]:
            return None
        elif type(xs) == str:
            return xs[xs.find(item)+1]
        else:
            return xs[xs.index(item)+1]
            
    primer_paso = next(xs)
    segundo_paso = next(xs)
    steps = segundo_paso - primer_paso
    
    if (item in xs) and ((item + steps) in xs) :
        return item + steps
    else:
        return None
