n = int(input())
a = [int(i) for i in input().split() if int(i) < 0]
x = int(input())
a.sort(reverse=True)
na = len(a)
if x == 0:
    print(0)
elif x <= na:
    c = na - x
    print(-a[c] * x + sum([a[c] - i for i in a[c + 1:]]))
else:
    print(-sum(a))
