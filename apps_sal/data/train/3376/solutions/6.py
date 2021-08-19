def square_free_part(n):
    if not isinstance(n, int):
        return None
    if n < 1:
        return None
    for i in range(n, 1, -1):
        if not n % i:
            b = True
            for j in range(i // 2, 1, -1):
                if not i % (j * j):
                    b = False
                    break
            if b:
                return i
