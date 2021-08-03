def alpha_seq(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    l = []
    for i in sorted(string):
        l.append(i.capitalize() + i * (alpha.find(i)))
    return ','.join(l)
