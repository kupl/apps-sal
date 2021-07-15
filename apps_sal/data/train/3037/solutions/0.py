from collections import Counter
def obtain_max_number(arr):
    c = Counter(arr)
    while 1:
        find = next((k for k in c if c[k] > 1), None)
        if not find:return max(c)
        c[find] -= 2
        c[find*2] = c.get(find*2,0) + 1
