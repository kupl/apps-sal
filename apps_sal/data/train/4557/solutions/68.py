def row_weights(l):
    li_eve = []
    li_odd = []
    for i in range(0, len(l)):
        if i % 2 == 0:
            li_eve.append(l[i])
        else:
            li_odd.append(l[i])
    return (sum(li_eve), sum(li_odd))
