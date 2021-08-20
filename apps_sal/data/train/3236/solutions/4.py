def my_crib(n):
    crib = [f"{mult(n * 2)}{mult(n * 2 + 1, '_')}{mult(n * 2)}"]
    crib.extend((f"{mult(n * 2 - i - 1)}/{mult((n + i) * 2 + 1, '_')}\\{mult(n * 2 - i - 1)}" for i in range(n * 2)))
    crib.extend((f'|{mult(n * 6 - 1)}|' for _ in range(n - 1)))
    crib.append(f"|{mult(n * 2)}{mult(n * 2 - 1, '_')}{mult(n * 2)}|")
    crib.extend((f'|{mult(n * 2 - 1)}|{mult(n * 2 - 1)}|{mult(n * 2 - 1)}|' for _ in range(n - 1)))
    crib.append(f"|{mult(n * 2 - 1, '_')}|{mult(n * 2 - 1, '_')}|{mult(n * 2 - 1, '_')}|")
    return '\n'.join(crib)


def mult(n, char=' '):
    return char * n
