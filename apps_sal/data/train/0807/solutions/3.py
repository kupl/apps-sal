for _ in range(int(input())):
    (n, q) = map(int, input().split())
    l = [int(i) for i in input().split()]
    qry = [int(input()) for i in range(q)]

    def cmp(sub1, sub2):
        for i in range(len(sub1)):
            if sub1[i] > sub2[i]:
                return 1
            if sub1[i] < sub2[i]:
                return 2
        return 1
    maxl = []
    for i in range(n):
        for j in range(i, n):
            maxl.append(max(l[i:j + 1]))
    maxl.sort(reverse=True)
    for i in qry:
        print(maxl[i - 1])
