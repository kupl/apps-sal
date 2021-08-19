nkm = list(map(int, input().split(' ')))
n = nkm[0]
k = nkm[1]
m = nkm[2]
li = list(map(int, input().split(' ')))
i = k - 1
j = k - 1
t = 1
c = 0
while i < n:
    if li[i] != 0:
        c += 1
        j = k - 1
        i = i + 2 * k - 1
    else:
        i -= 1
        j -= 1
        if j < 0:
            t = 0
            break
if t == 1:
    print(c)
else:
    print('-1')
