def magic_sum(arr):
    return sum(n for n in arr if n % 2 and '3' in str(n)) if arr else 0
