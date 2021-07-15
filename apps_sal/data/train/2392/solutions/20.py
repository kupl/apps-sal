from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    
    n //= m
    m %= 10
    
    part_sum = [0 for i in range(10)]
    res = 0
    
    for i in range(1, 10):
        part_sum[i] = (m*i)%10+part_sum[i-1]
        res += (m*i)%10
        
    a, b = (n // 10), (n%10)
    
    
    res *= a
    res += part_sum[b]
    
    print(res)
