# cook your dish here
for _ in range(int(input())):
    q = int(input())
    arr = list(map(int, input().split()))
    t = max(arr)
    for i in range(q - 1, -1, -1):
        if(arr[i] == t):
            r = i
            break
    for i in range(q):
        if(arr[i] == t):
            r = r - i
            break
    if((q // (1 + 1)) - r < 0):
        print(0)
    else:
        print((q // (1 + 1)) - r)
