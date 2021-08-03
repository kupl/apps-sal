
def comb(i):
    res = 1
    for k in range(1, i, 2):
        res = res * k
    print(res)


t = eval(input())
for i in range(1, t + 1):
    h = eval(input())
    h = h + 1
    comb(2 * h - 1)
