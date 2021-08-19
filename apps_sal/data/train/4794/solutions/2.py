def comfortable_numbers(l, r):

    def digit(n):
        sum = 0
        while n > 9:
            sum += n % 10
            n //= 10
        return sum + n
    a = [(x, y) for x in range(l, r) for y in range(x + 1, r + 1) if x <= y + digit(y) and x >= y - digit(y) and (y <= x + digit(x)) and (y >= x - digit(x))]
    return len(a)
