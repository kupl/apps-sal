n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
s, j, all_res = 0, 0, []
for i, q in enumerate(arr, 1):
    if s - j * (n - i) * q < k:
        all_res.append(str(i))
    else:
        s += q * j
        j += 1
print('\n'.join(all_res))
