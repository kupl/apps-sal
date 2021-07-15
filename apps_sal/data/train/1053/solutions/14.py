t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    arr.sort()
    i = 0
    while arr[i] != 1:
        i += 1
    print(i)
