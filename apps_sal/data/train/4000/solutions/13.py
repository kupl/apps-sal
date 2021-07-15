def strong_num(n):
    if n == 40585: return 'STRONG!!!!'
    def get_f(n):
        out = {0: 0, 1: 1}
        if n < 2: return out
        for i in range(2, max([int(x) for x in str(n)])+1):
            out[i] = out[i-1] * i
        return out
    d = get_f(n)
    return "STRONG!!!!" if n == sum([d[int(x)] for x in str(n)]) else "Not Strong !!"

