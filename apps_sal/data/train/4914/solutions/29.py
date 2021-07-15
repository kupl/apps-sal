def position(alphabet):
    a = 'abcdefghijklmnopqrstuvwxyz'
    x = list(map(lambda x: a[x],range(len(a)))).index(alphabet)+1
    return "Position of alphabet: "+str(x)
