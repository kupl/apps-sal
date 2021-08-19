
def Sieve(n):
    ret = []
    divlis = [-1] * (n + 1)

    flag = [True] * (n + 1)
    flag[0] = False
    flag[1] = False

    ind = 2
    while ind <= n:

        if flag[ind]:
            ret.append(ind)

            ind2 = ind ** 2

            while ind2 <= n:
                flag[ind2] = False
                divlis[ind2] = ind
                ind2 += ind

        ind += 1

    return ret, divlis


sev, divlis = Sieve(210000)

n = int(input())
a = list(map(int, input().split()))

dic = {}

for i in range(n):

    nd = {}

    na = a[i]
    while divlis[na] != -1:

        if divlis[na] not in nd:
            nd[divlis[na]] = 0
        nd[divlis[na]] += 1

        na //= divlis[na]

    if na != 1:
        if na not in nd:
            nd[na] = 1
        else:
            nd[na] += 1

    for x in nd:
        if x not in dic:
            dic[x] = []
        dic[x].append(nd[x])

ans = 1

for i in dic:

    if len(dic[i]) < n - 1:
        #print (i,"a")
        continue

    dic[i].sort()

    if len(dic[i]) == n:
        ans *= i ** dic[i][1]
        #print (i,"b")
    else:
        ans *= i ** dic[i][0]
        #print (i,"c")

print(ans)
