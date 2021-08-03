t = int(input())
modval = (10**9) + 7
for _ in range(t):
    val = list(input())
    inp = 0
    res = 0
    multiplier = 1
    for i in val:
        inp = ((inp * 10) + int(i)) % modval
        multiplier = (multiplier * 10) % modval
    for i in val:
        res = ((res * multiplier) + inp) % modval
        inp = (inp * 10 - (multiplier - 1) * int(i)) % modval
    print(res)
