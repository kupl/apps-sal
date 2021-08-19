t = int(input())
for ts in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    li = []
    for i in l:
        if i not in li:
            li.append(i)
    li.sort()
    print('yes' if li == [1, 2, 3, 4, 5, 6, 7] and l == l[::-1] else 'no')
