def magic_sum(arr):
    return 0 if not arr else sum(x for x in arr if x % 2 and '3' in str(x))
