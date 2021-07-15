def magic_sum(arr):
    return sum(v for v in arr if "3" in set(str(v)) and v%2) if arr else 0
