def find(n):
    total = 0
    for num in range(n + 1):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total
