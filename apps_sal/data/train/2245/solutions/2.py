def read_input():
    return list(map(int, input().split()))


(n, m, k) = read_input()
init_array = read_input()
operations = [read_input() for _ in range(m)]
additionals = [0] * (m + 1)
sums = [0] * (n + 1)
for _ in range(k):
    (x, y) = read_input()
    additionals[x - 1] += 1
    additionals[y] -= 1
sum_so_far = 0
for i in range(m):
    (l, r, val_to_add) = operations[i]
    sum_so_far += additionals[i]
    sums[l - 1] += sum_so_far * val_to_add
    sums[r] -= sum_so_far * val_to_add
sum_so_far = 0
for i in range(n):
    sum_so_far += sums[i]
    init_array[i] += sum_so_far
print(' '.join(map(str, init_array)))
