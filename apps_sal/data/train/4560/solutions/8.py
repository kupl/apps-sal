def answer(q, i):
    return (lambda p=__import__('re').compile('\\b(%s)\\b' % '|'.join(set(q.lower().split())), __import__('re').I): (lambda m=max(((j, len(p.findall(j))) for j in i), key=lambda t: t[1]): m[0] if m[1] else None)())()
