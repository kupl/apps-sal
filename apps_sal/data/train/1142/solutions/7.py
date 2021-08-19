def ff(l, x):
    if x == max(l):
        return 1
    elif x == min(l):
        return len(l)
    else:
        ls = l
        ls.sort(reverse=True)
        return ls.index(x) + 1


n = int(input())
li = []
r = n * [1]
for i in range(0, n):
    x = int(input())
    li.append(x)
    print(ff(li, x))
