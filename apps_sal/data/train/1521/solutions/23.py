t = int(input())

for _ in range(t):
    n = int(input())
    dell = []
    for __ in range(n):
        dell.append(list(map(int, input().split())))
    l = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            s1 = dell[i]
            s2 = dell[j]

            if (s1[0] <= s2[0] and s1[1] > s2[1]) or (s1[0] < s2[0] and s1[1] >= s2[1]):
                l[i][j] += 2

            elif (s2[0] <= s1[0] and s2[1] > s1[1]) or (s2[0] < s1[0] and s2[1] >= s1[1]):
                l[j][i] += 2

            else:
                l[i][j] += 1
                l[j][i] += 1

    for ele in l:
        print(sum(ele), end=" ")
    print()
