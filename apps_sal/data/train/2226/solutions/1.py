n = int(input())
a = list(map(int, input()))
acc = 0
back = 0
top = 0
cur = 0
s = []
for (i, x) in enumerate(a):
    if x == 0:
        cur = 0
    else:
        if cur > 0:
            s.pop()
        cur += 1
        if cur >= top:
            top = cur
            back = (cur + 1) * cur // 2 + (i - cur + 1) * cur
            s = [(cur, i)]
        else:
            back += i - (s[-1][1] - cur + 1)
            if cur >= s[-1][0]:
                s.pop()
            s += [(cur, i)]
    acc += back
print(acc)
