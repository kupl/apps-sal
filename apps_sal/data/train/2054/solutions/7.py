n = int(input())
es = []
rs = []
for i in range(n-1) :
    es.append(list(map(int , input().split())))
vs = list(map(int , input().split()))
for i in es :
    if vs[i[0] -1 ] != vs[i[1] - 1 ] :
        rs.append(i)
if rs == [] :
    print('YES')
    print(1)
    return
for r1 in rs[0] :
    for i in rs :
        if r1 != i[0] and r1 != i[1] :
            break
    else :
        print('YES')
        print(r1)
        return
print('NO')
