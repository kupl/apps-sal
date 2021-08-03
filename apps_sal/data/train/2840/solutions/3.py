bills = [[0, 0], [1, 3], [0, 1], [1, 4], [0, 2], [1, 0], [0, 3], [1, 1], [0, 4], [1, 2]]


def withdraw(n):
    q, r = divmod(n, 100)
    if r == 10 or r == 30:
        q -= 1
    return [q] + bills[r // 10]
