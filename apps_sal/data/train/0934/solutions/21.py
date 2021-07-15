t = int(input()) 
mod = 10 ** 9 + 7
for _ in range(t):
    p, q, r = map(int, input().split()) 
    A = sorted(int(x) for x in input().split()) 
    B = sorted(int(x) for x in input().split()) 
    C = sorted(int(x) for x in input().split()) 
    m = n = a = b = ans = 0
    for Y in B:
        while m < p and A[m] <= Y:
            a += A[m]
            m += 1 
        while n < r and C[n] <= Y:
            b += C[n]
            n += 1 
        ans += (Y * m + a) * (Y * n + b) 
        ans %= mod 
    print(ans)
        
        
