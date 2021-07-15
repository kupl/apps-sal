# cook your dish here
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    arr_k = list(map(int, input().split()))[:k]
    total_p = (n * m * (n + 1) * (m + 1)) // 4
    total = 0
    for i in range(k):
        a = arr_k[i]
        x = (a-1) // m + 1
        y = (a-1) % m + 1
        total += (x*y)*(n-x+1)*(m-y+1)
    res = total/total_p
    print(f'{res:.10f}')
