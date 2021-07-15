def sum_str(a: str, b: str) -> str:
    return str(int(a) + int(b) if a and b else a if a else b if b else 0)
