
tt = int(input())

for loop in range(tt):

    n = int(input())
    s = input()
    d = 0

    ans = 0
    for i in s:
        if i == "(":
            d += 1
        else:
            d -= 1

        if d < 0:
            ans += 1
            d = 0

    print(ans)
