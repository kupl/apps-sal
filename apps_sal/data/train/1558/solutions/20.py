# cook your dish here
for _ in range(int(input())):
    r, c = map(int, input().split())
    count = 0
    for i in range(0, r * c):
        ans = list()
        for x in range(0, r * c, i + 1):
            a = x // r
            b = x % r
            ans.append((a, b))
            a = x % c
            b = x // c
            ans.append((a, b))

        print(len(set(ans)), end=" ")
