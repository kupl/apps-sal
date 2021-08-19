N = int(input())
c = 0
while N > 0:
    c = c + 1
    N = N // 10
if c <= 3:
    print(c)
elif c > 3:
    print('More than 3 digits')
