(n, s) = (int(x) for x in input().split())
arr = [int(x) for x in input().split()]
less = sorted([x for x in arr if x < s], reverse=True)
more = sorted([x for x in arr if x > s])
if len(less) == len(more):
    print(0)
    quit()
eq_nr = len(arr) - len(less) - len(more)
target = []
count = eq_nr
idx = 0
operations = 0
if len(less) > len(more):
    target = less
    count += len(more)
else:
    target = more
    count += len(less)
while count < (n + 1) // 2:
    operations += abs(target[idx] - s)
    count += 1
    idx += 1
print(operations)
