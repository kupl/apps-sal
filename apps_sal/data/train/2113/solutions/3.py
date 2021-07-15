def merge_sort(a, l, r):
  res = 0
  if l < r:
    m = (l + r) // 2
    res += merge_sort(a, l, m)
    res += merge_sort(a, m + 1, r)
    
    i = l
    j = m + 1
    b = []
    while i <= m and j <= r:
      if a[i] <= a[j]:
        b.append(a[i])
        i += 1
      else:
        b.append(a[j])
        j += 1
        res += m - i + 1

    while i <= m:
      b.append(a[i])
      i += 1

    while j <= r:
      b.append(a[j])
      j += 1
    
    for idx, val in enumerate(b):
      a[idx + l] = val
      
  return res 

input()
a = [int(x) for x in input().split()]
n = len(a)
ans = merge_sort(a, 0, n - 1)
if ans & 1 == 0:
  ans *= 2
else:
  ans = ans * 2 - 1
print(ans)

