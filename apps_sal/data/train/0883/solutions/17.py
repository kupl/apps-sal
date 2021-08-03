# cook your dish here
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = []
    s.append(a[0])
    for i in range(1, n):
        if(a[i] != a[i - 1]):
            s.append(a[i])
    if(len(s) > 2):
        print(-1)
    else:
        if(len(s) == 1):
            if(s[0] == 0):
                print(n)
            else:
                if(s[0] == n - 1):
                    print(0)
                else:
                    print(-1)
        else:
            p = a.count(s[0])
            if(s[1] - s[0] != 1):
                print(-1)
            else:
                if(p == s[0] + 1):
                    print(n - p)
                else:
                    print(-1)
