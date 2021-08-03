def binary_gcd(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == 0 or y == 0:
        return bin(max(abs(x), abs(y))).count('1')
    for i in range(min(abs(x), abs(y)), 0, -1):
        if (x % i == 0 and y % i == 0):
            return bin(i).count('1')
