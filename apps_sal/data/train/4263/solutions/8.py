def apparently(string):
    a, r = string.split(), []
    for i in range(len(a)):
        if a[i] in ('and', 'but') and i == len(a)-1: r.append(a[i]+' apparently')
        elif a[i] in ('and', 'but') and a[i+1] != 'apparently': r.append(a[i]+' apparently')
        else: r.append(a[i])
    return ' '.join(r)
