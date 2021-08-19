def powers_of_two(n):
    result = []

    for i in range(n + 1):
        result.append(2 ** i)

    return result

# powers_of_two = lambda n: list(map(lambda i: 2 ** i, list(range(n + 1))));
