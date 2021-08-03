# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if(a[i] % 2 == 0):
            for j in range(i + 1, n):
                if(a[i] % 2 == 0 and a[j] % 2 != 0):
                    c += 1
    print(c)
