from string import ascii_lowercase as A
def cipher(phrase: str):
    a = A*2 + ' '*26
    seq = lambda n: n%3 + n//3 + (n%3>0) - (n>0)
    cip = lambda i: a[a.index(phrase[i]) + seq(i)]
    return ''.join(map(cip, range(len(phrase))))
