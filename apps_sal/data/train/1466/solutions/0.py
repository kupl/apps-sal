(n, q) = map(int, input().split())
ls = [int(i) for i in input().split()]
cur = 0
s = [0]
for i in ls:
    cur = cur ^ i
    s.append(cur)
for i in range(q):
    k = int(input())
    print(s[k % (n + 1)])
