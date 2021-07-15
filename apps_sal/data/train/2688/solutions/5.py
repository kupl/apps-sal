def repeat_sequence_len(n):
    f = lambda n: sum(int(c) ** 2 for c in str(n))
    tortoise = n
    rabbit = f(n)
    while tortoise != rabbit:
        tortoise = f(tortoise)
        rabbit = f(f(rabbit))
    rabbit = f(rabbit)
    result = 1
    while tortoise != rabbit:
        rabbit = f(rabbit)
        result += 1
    return result
