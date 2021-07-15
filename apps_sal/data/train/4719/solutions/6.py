def sort_array(lst):
    s = sorted(lst)
    even = (n for n in s[::-1] if n & 1 == 0)
    odd = (n for n in s if n & 1)
    return [next(odd if n & 1 else even) for n in lst]
