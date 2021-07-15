def bingo(c, n):
    r=range(5)
    q=[[(x in [int(w[1:])for w in n])or x=='FREE SPACE'for x in l]for l in c[1:]]
    return any(all(x)for x in[l for l in q]+[[l[i]for l in q]for i in r]+[[q[i][i]for i in r]]+[[q[i][4-i]for i in r]])
