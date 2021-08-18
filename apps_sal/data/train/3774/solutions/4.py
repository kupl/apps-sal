def is_prime(num):

    num = abs(int(num))

    if num < 2:
        return False

    if num == 2:
        return True

    if not num & 1:
        return False

    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False

    return True
