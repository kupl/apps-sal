st, k = input().split()

st = list(st)

k = int(k)
for i in range(len(st)):
    if (k < 1):
        break

    if (st[i] != '9'):

        st[i] = '9'

        k -= 1

print(''.join(st))
