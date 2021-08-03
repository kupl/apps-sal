t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = ""
    for i in range(len(a)):
        if(a[i] % k == 0):
            s = s + "1"
        else:
            s = s + "0"
    print(s)
