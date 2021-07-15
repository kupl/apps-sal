def magic_sum(arr):
    return sum(i for i in arr if '3' in str(i) and i%2) if arr else 0
