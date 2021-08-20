def find_variable():
    d = globals()
    for x in d['VVV']:
        if d[x] == 777:
            return x
