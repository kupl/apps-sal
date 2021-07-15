def find_multiples(integer, limit):
    l = []
    for x in range(integer,limit+1):
        if(x % integer == 0):
            l.append(x)
    return l
