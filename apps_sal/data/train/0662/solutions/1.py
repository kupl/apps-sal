# cook your dish here
t = int(input())
while t > 0:
    d = int(input())
    l, r = map(int, input().split())
    if l % 2 == 1 and r % 2 == 1:
        num = (r - l) // 2 + 1
    elif l % 2 == 1 or r % 2 == 1:
        num = (r - l + 1) // 2
    else:
        num = (r - l) // 2
    if l % 2 == 0:
        l = l + 1
    if(num % (2 * d) == 0):
        n = num // (2 * d)
    else:
        n = num // (2 * d) + 1
    init = l * d + d * (d - 1)
    su = n * init
    su = su + 2 * d * d * n * (n - 1)
    print(su % 1000000007)
    t = t - 1
