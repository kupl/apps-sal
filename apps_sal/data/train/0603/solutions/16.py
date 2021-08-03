s = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
for i in range(t):
    s1 = ''
    n = int(input())
    while(1):
        s1 = s[n::-1] + s1
        if(n < 26):
            break
        n = n - 25
    print(s1)
