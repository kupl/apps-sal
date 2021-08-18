from sys import stdin
z = ['a', 'i', 'e', 'o', 'u']
t = int(stdin.readline())
while(t > 0):
    t -= 1
    n = int(stdin.readline())
    alice = []
    bob = []
    for j in range(n):
        s = str(stdin.readline().strip("\n"))
        isalice = True
        for i in range(1, len(s) - 1):
            if(s[i] in z):
                if(s[i - 1] not in z and s[i + 1] not in z):
                    isalice = False
            else:
                if(s[i - 1] not in z or s[i + 1] not in z):
                    isalice = False
            if(not isalice):
                break
        if(s[0] not in z and s[1] not in z):
            isalice = False
        if(s[-1] not in z and s[-2] not in z):
            isalice = False
        if(isalice):
            alice.append(s)
        else:
            bob.append(s)
    ali = {}
    bo = {}
    for i in alice:
        d = {}
        for j in i:
            if(j in d):
                d[j] += 1
            else:
                d[j] = 1
        for j in d:
            if j not in ali:
                ali[j] = (1, d[j])
            else:
                ali[j] = (ali[j][0] + 1, ali[j][1] + d[j])
    for i in bob:
        d = {}
        for j in i:
            if(j in d):
                d[j] += 1
            else:
                d[j] = 1
        for j in d:
            if j not in bo:
                bo[j] = (1, d[j])
            else:

                bo[j] = (bo[j][0] + 1, bo[j][1] + d[j])
    ans = 1
    for i in ali:
        ans *= ali[i][0]
    for i in bo:
        ans = ans / bo[i][0]
    x = 1
    y = 1

    for i in bo:
        x = x * bo[i][1]
    for i in ali:
        y = y * ali[i][1]
    alice = len(alice)
    bob = len(bob)
    for i in range(bob):
        while(alice > 0 and ans > 10000000):
            ans = ans / y
            alice -= 1
        ans *= x
        if(ans > 10000000 and alice == 0):
            break
    while(alice > 0):
        ans = ans / y
        if(ans < 1 and alice > 100):
            ans = 0
            break
        alice -= 1
    if(ans > 10000000):
        print("Infinity")
    else:
        print(ans)
