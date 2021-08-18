def pairwise(arr, n):
    save = set()
    add = save.add
    return sum(i + j if x + y == n and not (i in save or add(j) or add(i)) else 0 for i, x in enumerate(arr) if i not in save for j, y in enumerate(arr[i + 1:], i + 1) if j not in save)
