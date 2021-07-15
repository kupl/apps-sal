no_zeb = int(input())
lst = []
for _ in range(no_zeb):
    position, dist = (list(map(int, input().split())))
    lst.append((position, dist))
for j in lst:
    spit_i = j[0] + j[1]
    for l in lst:
        if l[0] == spit_i and l[0] + l[1] == j[0]:
            print('YES')
            return
print('NO')

