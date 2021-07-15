from collections import Counter

def find_dups_miss(arr):
    mi, ma, c = min(arr), max(arr), Counter(arr)
    duplicates = sorted(n for n in c if c[n] > 1)
    return [ma*(ma+1)//2 - mi*(mi-1)//2 - sum(c), duplicates]
