# cook your dish here
import random
def miller_rabin(n, k):

    if n == 2 or n==3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
pows = {1:2}
n, k = list(map(int, input().split(' ')))
T = pow(2,n)
if miller_rabin(n,6):
    print((T-2)%k)
else:
    m = 0
    for i in range(2,n//2+1):
        if n%i==0:
            if i>50000:
                a = 6
            elif i>20000:
                a = 5
            else:
                a = 4
            if miller_rabin(i,a):
                pows[i]=pow(2,i)-2
                m+=pows[i]
            else:
                w = 0
                for j in pows:
                    if i%j==0:
                        w+=pows[j]
                    if j>i//2:
                        break
                pows[i] = pow(2,i)-w
                m+=pows[i]

    print((T-m-2)%k)

