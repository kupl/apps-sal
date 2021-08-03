# cook your dish here
def ans(p):
    pika = (p * (p + 1)) // 2
    tmep = 1
    while(p >= 1):
        pika -= (p + 1) // 2 * tmep
        pika -= 1
        p //= 2
        tmep *= 2
    return pika


for _ in range(int(input())):
    l, r = map(int, input().split())
    print(ans(r) - ans(l - 1))
