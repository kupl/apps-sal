def next_item(xs, item):
    if xs.__class__.__name__ == 'listiterator': 
        while xs:
            try:
                 if next(xs) == item: return next(xs)
            except:
                 return
    elif xs.__class__.__name__ == 'count':
         return item+1
    try:
        return xs[xs.index(item)+1]
    except:
        return
