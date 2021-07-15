def atomic_number(electrons):
    result = []
    for i in range(1, 100):
        n = 2 * i * i
        result.append(min(electrons, n))
        electrons -= n
        if electrons <= 0:
            break
    return result
