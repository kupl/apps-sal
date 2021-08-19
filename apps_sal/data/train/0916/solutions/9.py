# cook your dish here
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


T = int(input())
while(T):
    l = [int(k) for k in input().split()]
    print(int((l[0] * l[1]) / gcd(l[0], l[1])))

    T -= 1
