from fractions import gcd

def DPC_sequence(s):
    res = 1
    
    for i, c in enumerate(s, 1):
        if c == 'D':
            res *= i // gcd(i, res)
            
    def check_DPC_at(i, c):
        if c == 'D':
            return gcd(i, res) == i
        elif c == 'C':
            return gcd(i, res) in range(2, i)
        elif c == 'P':
            return gcd(i, res) == 1
            
    return res if all(check_DPC_at(*e) for e in enumerate(s, 1)) else -1

