def compress(sentence):
    l = sentence.lower().split()
    d = {}
    ans = []
    for x in l:
        if not x in d:
            d[x] = len(d)
        ans += [str(d[x])]
    return ''.join(ans)
