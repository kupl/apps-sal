(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
set_a = {}
set_b = {}
for (index, item) in enumerate(a):
    if item not in set_a:
        set_a[item] = index
for (index, item) in enumerate(b):
    if item not in set_b:
        set_b[item] = index
sums = {}
total = 0
done = False
for (value_a, index_a) in set_a.items():
    for (value_b, index_b) in set_b.items():
        if value_a + value_b not in sums:
            sums[value_a + value_b] = True
            total += 1
            print(index_a, index_b)
            if total == n + m - 1:
                done = True
                break
    if done:
        break
