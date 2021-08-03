T = int(input())
for i in range(0, T):
    t = []
    count = 0
    a = input().split(" ")
    n = int(a[0])
    m = int(a[1])
    s = int(a[2])
    h = list(map(int, input().split(" ")))
    h1 = list(h)
    h1.sort()
    t = [x for x in h1 if x <= 2 * s]

    if len(t) == 0:
        print(0)

    else:

        count = sum([x <= s for x in t])
        if count >= m:
            print(m)
        else:
            print(count + (m - count) // 2)
