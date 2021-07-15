def dont_give_me_five(start,end):
    l = []
    for x in range(start, end+1):
        if '5' not in str(x):
            l.append(x)
    return len(l)
