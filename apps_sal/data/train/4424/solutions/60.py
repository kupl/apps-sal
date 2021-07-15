def expression_matter(a, b, c):
    return max(list(map(eval, gen(a, b, c))))

def gen(a, b, c):
    ops = ['+', '*']
    combs = []
    for i in ops:
        for j in ops:
            s = '%d %s %d %s %d' % (a, i, b, j, c)
            t = '(%d %s %d) %s %d' % (a, i, b, j, c)
            u = '%d %s (%d %s %d)' % (a, i, b, j, c)
            combs.append(s)
            combs.append(t)
            combs.append(u)
    return combs

