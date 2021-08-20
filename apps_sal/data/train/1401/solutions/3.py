(n, k) = list(map(int, input().split()))
x = [int(i) for i in input().split()]
x.sort()
s = 0
c = 0
for i in x:
    s += i
    if s <= k:
        c += 1
    else:
        break
print(c)
