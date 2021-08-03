def simplify(number: int) -> str:
    digits = str(number)
    res = [f"{n}*1{'0' * i}" for i, n in zip(list(range(len(digits) - 1, 0, -1)), digits) if n != '0']
    return '+'.join(res + ([digits[-1]] if digits[-1] != '0' else []))
