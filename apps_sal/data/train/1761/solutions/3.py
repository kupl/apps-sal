# That was the easy?
# - Cache is too slow (first version with bisect failed monsters)
# - Recursion is too deep
# - Formula is too imprecise
# I fear what the hard version will be x)

x, y, r, i, memo = 3, 4, 2, 0, []
for n in range(3, 100000):
    if n > x:
        _, _, x, r = memo[i]
        i += 1
    memo.append([y, r, y+r-1, n])
    y += r
        
def find(n):
    if n < 6: return [0, 1, 2, 2, 3, 3][n]
    x = 6
    for a, b, _, y in memo:
        if y * b >= n - x:
            return (n - x) // y + a
        x += y * b
