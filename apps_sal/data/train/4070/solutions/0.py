def magic_sum(arr):
    return arr and sum((x for x in arr if x % 2 and '3' in str(x))) or 0
