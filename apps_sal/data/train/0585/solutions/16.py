# cook your dish here
def gcd(a1, b1):
    if b1 == 0:
        return a1
    else:
        return gcd(b1, a1 % b1)


a = int(input())
for i in range(a):
    b = list(map(int, str(input()).split(' ')))
    c = list(map(int, str(input()).split(' ')))
    k = c[0]
    Ans = 0
    if b[0] == 1:
        print(0)
    else:
        if b[1] == 1:
            if b[0] > c[0]:
                print(abs(b[0] - c[0]))
            elif b[0] == c[0]:
                print(0)
            else:
                for i2 in range(b[0] - 1):
                    if (c[0] % b[0]) != 0:
                        Ans += 1
                        b[0] -= 1
                    else:
                        break
                print(Ans)

        else:
            for i1 in range(b[1]):
                k = gcd(c[i1], k)
            if b[0] > k:
                print(abs(b[0] - k))
            elif b[0] == k:
                print(0)
            else:
                for i3 in range(b[0] - 1):
                    if (k % b[0]) != 0:
                        Ans += 1
                        b[0] -= 1
                    else:
                        break
                print(Ans)
