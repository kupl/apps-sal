# cook your dish here
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    org_ratings = list(map(int, input().split()))
    l = []
    count = 0
    for i in range(n):
        l.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            if(j == 0):
                l[i][j] = l[i][j] + org_ratings[i]
            else:
                l[i][j] = l[i][j] + l[i][j - 1]
    # print(l)
    ranks = [[-1 for i in range(len(l[0]))] for j in range(len(l))]
    # print(ranks)
    for i in range(m):
        l2 = []
        for j in range(n):
            l2.append([l[j][i], j + 1])

        l2.sort(reverse=True, key=lambda x: x[0])

        for ind in range(len(l2)):
            if ind == 0:
                pos = 1
            else:
                if l2[ind][0] == l2[ind - 1][0]:
                    pos = ranks[l2[ind - 1][1] - 1][i]
                else:
                    pos = ind + 1
            ranks[l2[ind][1] - 1][i] = pos
    # print(ranks)
    for i in range(n):
        # print(ranks[i].index(min(ranks[i])))
        # print(l[i].index(max(l[i])))
        if l[i].index(max(l[i])) != ranks[i].index(min(ranks[i])):
            count += 1
    print(count)
