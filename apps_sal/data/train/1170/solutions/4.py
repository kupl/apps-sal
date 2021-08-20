t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    s = ''
    arr = list(map(int, input().split()))
    for z in range(n):
        if arr[z] % k == 0:
            s = s + '1'
        else:
            s = s + '0'
    print(s)
