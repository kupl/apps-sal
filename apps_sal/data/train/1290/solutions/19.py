n = int(input())
c = 0
while n > 0:
    c += 1
    n //= 10
if c == 1:
    print(1)
elif c == 2:
    print(2)
elif c == 3:
    print(3)
elif c > 3:
    print('More than 3 digits')
