def collatz(n):
    numbers = sequence(n)
    result = '->'.join(map(str, numbers))
    return result


def sequence(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + sequence(n // 2)
    else:
        return [n] + sequence(3 * n + 1)
