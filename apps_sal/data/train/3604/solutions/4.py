b = [False]
a = []
a2 = [None]

def f(n):
    def is_happy(n):
        s = {n}
        while n != 1:
            nn = 0
            while n > 0: nn += (n%10)**2; n//=10
            n = nn
            if n < len(b): return b[n]
            if n in s: return False
            s.add(n)
        return True
    for k in range(1, n+1):
        b.append(is_happy(k))
        if b[k]: a.append(k)
        a2.append(len(a))
f(300000)

def performant_numbers(n):
    return a[:a2[n]]
