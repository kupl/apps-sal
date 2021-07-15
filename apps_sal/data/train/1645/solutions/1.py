sq=lambda n: (n**0.5)%1==0

def sum_of_squares(n):
    if sq(n): return 1
    while not n&3: n>>=2
    if n&7==7: return 4
    for i in range(int(n**0.5)+1):
        if sq(n-i*i): return 2
    return 3
