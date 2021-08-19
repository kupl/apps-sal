from operator import itemgetter
(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
arr = []
dic = {}
two = []
for i in range(m):
    y = list(map(str, input().split()))
    a = int(y[0])
    b = int(y[1])
    flag = 0
    if a in x:
        two.append([b, y[2]])
    else:
        arr.append([b, y[2]])
for i in x:
    if i in dic:
        for j in dic[i]:
            print(j)
two = sorted(two, key=itemgetter(0), reverse=True)
arr = sorted(arr, key=itemgetter(0), reverse=True)
for i in two:
    print(i[1])
for i in arr:
    print(i[1])
'if a in dic:\n     dic[a].append(y[2])\n     flag=1\n    else:\n     dic[a]=[y[2]]\n     flag=1'
