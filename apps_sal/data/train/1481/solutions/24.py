t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    if(n % 2 == 1):
        print(-1)
    else:
        o = s.count('1')
        z = s.count('0')
        if(o == n or z == n):
            print(-1)
        else:

            print(n // 2 - min(o, z))
