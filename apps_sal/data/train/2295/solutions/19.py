n,*l = list(map(int,open(0).read().split()))
a = l[::2]
b = l[1::2]
print((0 if a==b else sum(a) - min(b[i] for i in range(n) if b[i] < a[i])))

