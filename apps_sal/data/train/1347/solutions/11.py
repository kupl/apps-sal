(n, m) = list(map(int, input().strip().split()))
spcl = [int(num) for num in input().strip().split()]
spclpost = [' '] * 100000
post = [' '] * 100000
for i in range(m):
    (f, p, s) = input().strip().split()
    f = int(f)
    p = int(p)
    if f in spcl:
        spclpost[p - 1] = s
    else:
        post[p - 1] = s
for j in range(100000, 0, -1):
    if spclpost[j - 1] != ' ':
        print(spclpost[j - 1])
for j in range(100000, 0, -1):
    if post[j - 1] != ' ':
        print(post[j - 1])
