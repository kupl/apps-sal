def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


n = eval(input())
a = list(map(int, input().split()))
for i in range(eval(input())):
    l, r = (int(x) for x in input().split())
    b = a[l - 1:r]
    c = []
    c = qsort(b)
    sum = 0
    for i in range(1, len(c)):
        j = c[i] - c[i - 1]
        sum += pow(j, 2)
    print(sum)
