t = int(input())


def gcd(a, b):

    if (a == 0):
        return b

    return gcd(b % a, a)


while(t > 0):
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    if(gcd(a, b) == 1):
        print("YES")
    else:
        print("NO")
    t -= 1
