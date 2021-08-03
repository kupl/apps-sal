# cook your dish here
t = int(input())
while(t > 0):
    n = int(input())
    cnt = 0
    cnt = n // (2**11)
    n %= (2**11)
    while(n > 0):
        num = n % 2
        cnt += num
        n //= 2
    print(cnt)
    t -= 1
