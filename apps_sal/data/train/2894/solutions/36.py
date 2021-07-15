def triple_trouble(one, two, three):
    x= list(zip(one,two,three))
    l1= [''.join(y) for y in x]
    return ''.join(l1)
