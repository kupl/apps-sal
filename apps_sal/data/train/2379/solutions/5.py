t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input()))

    zeros = []
    ones = []
    count = 0
    ans = []

    for d in s:
        if d == 0:
            if zeros:
                ans.append(zeros[-1])
                ones.append(zeros.pop())
            else:
                count += 1
                ans.append(count)
                ones.append(count)
        else:
            if ones:
                ans.append(ones[-1])
                zeros.append(ones.pop())
            else:
                count += 1
                ans.append(count)
                zeros.append(count)

    print(count)
    print(*ans)
