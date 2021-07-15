def solve(n):
    c = 0
    for i in range(min(8,n)+1):
        for j in range(min(4 if i!=0 else 8,n-i)+1):
            c += n-i-j+1
    return c
