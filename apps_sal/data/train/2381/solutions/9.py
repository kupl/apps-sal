
t = int(input())

for loop in range(t):

    s = input()

    ans = 0

    now = 0
    for i in s:

        if i == "R":
            now = 0
        else:
            now += 1
            ans = max(ans,now)

    print(ans + 1)

