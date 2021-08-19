# cook your dish here
for _ in range(int(input())):

    n = int(input())

    if n % 2 == 0:

        ans = []
        for i in range(1, n + 1, 2):
            ans.append(i + 1)
            ans.append(i)

    else:

        ans = []

        for i in range(1, n + 1 - 3, 2):
            ans.append(i + 1)
            ans.append(i)

        ans.extend([n - 1, n, n - 2])

    print(*ans)
