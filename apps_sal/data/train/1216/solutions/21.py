# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] >= x:
        print("YES")
    else:
        print('NO')
