jcash = {}


def splitlist(lst):

    def splitl(i, w):
        g = jcash.get((i, w))
        if g:
            return g
        if i == len(lst):
            return []
        wi = lst[i]
        a1 = splitl(i + 1, w)
        if wi > w:
            jcash[i, w] = a1.copy()
            return a1
        a2 = splitl(i + 1, w - wi)
        if sum(a1) < sum(a2) + wi:
            a2.append(wi)
            jcash[i, w] = a2.copy()
            return a2
        else:
            jcash[i, w] = a1.copy()
            return a1
    jcash.clear()
    lst.sort()
    lst.reverse()
    a = splitl(0, sum(lst) // 2)
    b = lst.copy()
    for i in a:
        b.remove(i)
    return (a, b)
