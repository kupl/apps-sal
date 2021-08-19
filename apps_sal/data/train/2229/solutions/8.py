def is_subsequence(a, b, idx, top):
    i = 0
    for j, c in enumerate(a):
        if c == b[i] and idx[j + 1] > top:
            i += 1
        if i == len(b):
            return True
    return False


a = input()
b = input()
r = list(map(int, input().split()))
idx = [0 for _ in range(len(r) + 1)]
for i in range(len(r)):
    idx[r[i]] = i

lo = -1
hi = len(a)
while hi - lo > 1:
    mi = (lo + hi) // 2
    if is_subsequence(a, b, idx, mi):
        lo = mi
    else:
        hi = mi

print(lo + 1)

# ~ for i in range(-1, len(r)+1):
#~ print(is_subsequence(a, b, idx, i))
