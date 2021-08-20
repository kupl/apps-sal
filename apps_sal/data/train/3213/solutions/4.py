def sum_of_a_beach(beach):
    b = beach.lower()
    l = ['sand', 'water', 'fish', 'sun']
    c = 0
    for w in l:
        if w in b:
            c += b.count(w)
    return c
