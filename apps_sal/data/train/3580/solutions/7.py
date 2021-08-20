def get_positions(n):
    num = n % 27
    return (num % 3, int(num % 3 ** 2 / 3 ** 1), int(num / 3 ** 2))
