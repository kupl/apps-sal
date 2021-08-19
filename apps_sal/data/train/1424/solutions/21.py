# cook your dish here
ab = input().split(' ')
a = ab[0]
b = int(ab[1])
aa = []
for x in str(a):
    aa.append(int(x))
while b > 0:

    if len(aa) == 1 and aa[0] == 0:
        break
    else:
        if aa[-1] == 0:

            del(aa[-1])

        else:

            aa[-1] = int(aa[-1]) - 1
    b -= 1
for x in aa:
    print(x, end='')
