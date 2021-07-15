vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))

def solution(n):
    if n == 0: return ""
    return next(c + solution(n-v) for c,v in vals if v <= n)
