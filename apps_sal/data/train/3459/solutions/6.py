def solve(n,k):
    n = str(n)
    number = ''
    while k < len(n):
        m = min([(int(n[i]), i) for i in range(k+1)])
        number += str(m[0])    
        n = n[m[1]+1:]
        k -= m[1]
    return number
