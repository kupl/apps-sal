import operator as op
input()
a = list((x[0] for x in sorted(enumerate(map(int, input().split())), key=op.itemgetter(1))))
ans = []
for i in range(len(a)):
    if a[i] != -1:
        j = a[i]
        a[i] = -1
        t = [i + 1]
        while j != i:
            t.append(j + 1)
            last = j
            j = a[j]
            a[last] = -1
        ans.append(t)
print(len(ans))
for i in range(len(ans)):
    print(len(ans[i]), *ans[i])
