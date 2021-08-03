from operator import itemgetter
n, d = int(input()), {}
a, b = sorted(map(int, input().split()), reverse=True), sorted(sorted(enumerate(map(int, input().split())), reverse=True), key=itemgetter(1))
for i in range(n):
    d[b[i][0]] = a[i]
for i in range(n):
    print(d[i], end=' ')
