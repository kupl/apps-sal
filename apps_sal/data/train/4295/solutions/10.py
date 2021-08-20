def balanced_num(number: int) -> str:
    d = list(map(int, str(number)))
    return 'Balanced' if sum(d[:(len(d) - 1) // 2]) == sum(d[len(d) // 2 + 1:]) else 'Not Balanced'
