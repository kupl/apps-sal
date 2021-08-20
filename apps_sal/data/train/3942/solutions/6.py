def solve(n):
    if n % 10 != 0:
        return -1
    count = 0
    while n >= 500:
        n -= 500
        count += 1
    while n >= 200:
        n -= 200
        count += 1
    while n >= 100:
        n -= 100
        count += 1
    while n >= 50:
        n -= 50
        count += 1
    while n >= 20:
        n -= 20
        count += 1
    while n >= 10:
        n -= 10
        count += 1
    return count
