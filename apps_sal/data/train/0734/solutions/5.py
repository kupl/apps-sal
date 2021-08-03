from collections import defaultdict


def caps(a):
    d = defaultdict(list)
    for i in range(len(a)):
        d[a[i]].append(i)
        if(len(d[a[i]]) > len(a) // 2):
            return('No', [])
    arr = []
    for i in d.keys():
        arr += ([i] * len(d[i]))
    arr2 = [i for i in arr]
    arr2 = arr2[len(a) // 2:] + arr2[:len(a) // 2]
    for i in range(len(arr2)):
        di = arr[i]
        vi = arr2[i]
        a[d[di][0]] = vi
        d[di].remove(d[di][0])
    return('Yes', a)


t = int(input())
for _ in range(t):
    n = input()
    a = input().split()
    ans, arr = caps(a)
    print(ans)
    if(ans == 'Yes'):
        st = ""
        for i in arr:
            st += i + ' '
        print(st)
