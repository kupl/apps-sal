def triple_trouble(one, two, three):
    l=[]
    for i in range(0,len(one)):
        l.append(one[i]+two[i]+three[i])
    return ''.join(l)
