# cook your dish here
n, k, p = map(int, input().split())
f = list(map(int, input().split()))
seq = sorted(set(f))
m = 0
seq1 = {seq[0]: 0}
for i in range(1, len(seq)):
    if seq[i] - seq[i - 1] > k:
        m += 1
    seq1[seq[i]] = m
while p > 0:
    i, j = map(int, input().split())
    i, j = f[i - 1], f[j - 1]
    if seq1[i] == seq1[j]:
        print('Yes')
    else:
        print('No')
    p -= 1
