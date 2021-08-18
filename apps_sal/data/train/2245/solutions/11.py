def int_list(s): return [int(n) for n in s.split(" ")]


n, m, k = int_list(input())
arr = int_list(input())
operations = [int_list(input()) for _ in range(m)]

incrs = [0] * len(arr)
freq = [0] * m

for _ in range(k):
    l, r = int_list(input())
    freq[l - 1] += 1
    if r < len(freq):
        freq[r] -= 1

times = 0
for i, op in enumerate(operations):
    l, r, d = op
    times += freq[i]
    incrs[l - 1] += times * d
    if r < len(incrs):
        incrs[r] -= times * d

prev = 0
for i, n in enumerate(arr):
    arr[i] = prev + n + incrs[i]
    prev += incrs[i]

print(" ".join([str(n) for n in arr]))
