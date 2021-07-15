# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if max(a) == 0:
            print(1)
        else:
            
            x = n
            for i in range(n):
                if a[i] == 0:
                    x-=1
                else:
                    break
            
            for j in range(n-1, -1, -1):
                if a[j] == 0:
                    x-=1
                else:
                    break
            print(x)
except EOFError:pass
