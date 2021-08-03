N = 10**9 + 7

t = int(input())
for _ in range(t):
    s = str(input())

    if(s[0] == '0'):
        print(0)
    else:
        x = len(s)
        a = [1] * (x + 1)
        for i in range(2, x + 1):
            if(s[i - 1] == '0'):
                if(s[i - 2] == '1' or s[i - 2] == '2'):
                    a[i] = a[i - 2]
                else:
                    a[x] = 0
                    break
            elif(s[i - 1] == '7' or s[i - 1] == '8' or s[i - 1] == '9'):
                if(s[i - 2] == '1'):
                    a[i] = a[i - 1] + a[i - 2]
                else:
                    a[i] = a[i - 1]
            else:
                if(s[i - 2] == '1' or s[i - 2] == '2'):
                    a[i] = a[i - 1] + a[i - 2]
                else:
                    a[i] = a[i - 1]
            a[i] = a[i] % N

        print(a[x])
