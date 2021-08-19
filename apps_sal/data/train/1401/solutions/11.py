# cook your dish here
n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
p = 0
c = 0
for i in l:
    if p + i >= k:
        break
    else:
        p += i
        c += 1
print(c)
