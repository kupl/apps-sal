(n, k, p) = [int(i) for i in input().split()]
n_sep = list(map(int, input().split()))
count = 0
sep_sort = sorted(n_sep)
hashing = {sep_sort[0]: 0}
for j in range(1, n):
    if abs(sep_sort[j] - sep_sort[j - 1]) > k:
        count += 1
    hashing[sep_sort[j]] = count
for i in range(p):
    pair = list(map(int, input().split()))
    if hashing[n_sep[pair[1] - 1]] == hashing[n_sep[pair[0] - 1]]:
        print('Yes')
    else:
        print('No')
