def find(n):
    return sum((loop for loop in range(1, n + 1) if not loop % 3 or not loop % 5))
