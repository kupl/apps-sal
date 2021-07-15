def odd(s):
    r = [i for i in s.lower() if i == 'o' or i == 'd']
    result = []
    while True:
        word = ''
        try:
            o = r.index('o')
            d = r[o+1:].index('d')+o+1
            d2 = r[d+1:].index('d')+d+1
            word += r.pop(d2)+ r.pop(d)+r.pop(o)
            if word[::-1] == "odd":
                result.append(word)
        except Exception:
            break
    return len(result)
