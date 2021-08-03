a = input()
b = input()

acount = a.count('1')
bcount = b.count('1')

if (acount % 2 == 1):
    acount += 1

if (acount >= bcount):
    print('YES')
else:
    print('NO')
