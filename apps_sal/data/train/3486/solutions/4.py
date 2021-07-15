def find_last(n, m):
    people = list(range(1, n + 1))
    coins = 0
    for staying in range(n, 1, -1):
        if staying >= m:
            people = people[m:] + people[:m - 1]
            coins += m + (staying - m) * 2
        else:
            last = (m % staying - 1) % staying
            people = people[last + 1:] + people[:last]
            coins += m
    return people[0], coins
