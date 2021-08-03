n = int(input())
for i in range(n):
    s = input()
    res = []
    for i in set(s):
        res.append(s.count(i))

    res.sort()

    if len(res) < 3 or res[-1] == res[-2] + res[-3]:
        print("Dynamic")

    else:
        print("Not")
