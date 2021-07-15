#using lucas's theorem https://en.wikipedia.org/wiki/Lucas%27s_theorem

def to_bin(n):
    k = 0
    while n >= 2**k: k += 1
    s = ""
    for i in range(k - 1, -1, -1):
        if n - 2**i >= 0: 
            s += "1"
            n -= 2**i
        else: s += "0"
    return s

def subsets_parity(n, k):
    s1 = to_bin(n)
    s2 = to_bin(k)
    for i in range(-1, -len(s2) - 1, -1):
        if s1[i] == "0" and s2[i] == "1": return "EVEN"
    return "ODD"
