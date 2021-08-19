# cook your dish here
t = int(input())


def gcd(a, b):
    big = max(a, b)
    small = min(a, b)
    while small:
        big, small = small, big % small
    return(big)


for __ in range(t):
    a, b = list(map(int, input(). split(" ")))
    print(gcd(a, b))
