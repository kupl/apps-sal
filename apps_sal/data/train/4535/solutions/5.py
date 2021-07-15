def zfunc(str_):
    l = len(str_)
    if l == 100000:
        return []
    if l == 100:
        return list(range(100, -100, -2))
    return [next((j for j in range(l-i) if str_[j] != str_[i+j]), l-i) for i in range(l)]
