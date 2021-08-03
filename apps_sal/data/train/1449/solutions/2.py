#import psyco
# psyco.full()

for _ in range(int(input())):
    s = input().strip()
    ways = 0
    l = len(s)

    index = []
    for i in range(l):
        if s[i] == '4':
            index.append(i)
    if len(index) == 0:
        print(0)
    else:
        ways = 0
        ways += (index[0] + 1 - 0) * (l - index[0])
        for i in range(1, len(index)):
            ways += (index[i] - index[i - 1]) * (l - index[i])

        print(ways)
