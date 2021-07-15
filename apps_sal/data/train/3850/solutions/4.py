def close_to_zero(t):
    T=[int(v) for v in t.split()]
    return T and sorted(sorted(T,reverse=True),key=abs)[0] or 0
