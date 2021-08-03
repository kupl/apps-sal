# cook your dish here
try:
    m, n = map(int, input().split())
    arr_m = list(map(int, input().split()))
    arr_n = list(map(int, input().split()))
    Sum = 0
    s = set()
    for i in range(m):
        for j in range(n):
            if len(s) > (m + n - 2):
                break
            Sum = arr_m[i] + arr_n[j]
            if Sum not in s:
                s.add(Sum)
                print(i, j)

except:
    pass
