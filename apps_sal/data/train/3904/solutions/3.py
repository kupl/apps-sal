def is_divisible_by_6(s):
    if s[-1] in "13579":
        return []
    l, base, step = s.count("*"), int(s.replace("*", "0")), (6 if s[-1] == "*" else 3)
    start, s = next(n for n in range(base, base + step) if n % step == 0) - base, s.replace("*", "{}")
    return [s.format(*f"{rep:0{l}d}") for rep in range(start, 10**l, step)]
