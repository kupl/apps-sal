def hotpo(n):
    nb_exec = 0
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        nb_exec += 1
    return nb_exec
