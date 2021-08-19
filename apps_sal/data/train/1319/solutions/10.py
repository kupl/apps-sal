from bisect import insort
(n, m) = list(map(int, input().split()))
pos = []
count = 0
while count < m:
    i = int(input())
    if i > 0:
        insort(pos, i)
    else:
        print(pos.pop(-1))
        count += 1
