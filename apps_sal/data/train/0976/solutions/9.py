n = int(input())
it = list(map(int, input().split()))
maa = 0
ma = 0
j = 0
dd = 0
ss = {}
mi = 0
a = []
b = []
for i in it:
    i -= 1
    if i == 1 or i == 3:
        c = a.pop()
        d = b.pop()
        if i == 1:
            maa = max(maa, j - c[1] + 1)
        else:
            mi = max(mi, j - c[1] + 1)
    else:
        if a == []:
            a.append([i, j])
            b.append(1)
        else:

            if i == a[-1][0]:

                b.append(b[-1])
            else:
                b.append(b[-1] + 1)
            a.append([i, j])
    if b:
        ma = max(ma, b[-1])
    j += 1

print(ma, maa, mi)
