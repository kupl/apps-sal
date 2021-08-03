t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    li = []
    for j in l:
        if j not in li:
            li.append(j)
    li.sort()
    print('yes' if (li == [1, 2, 3, 4, 5, 6, 7] and l == l[::-1]) else 'no')
