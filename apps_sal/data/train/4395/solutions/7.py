def next_higher(n):
    b = f"0{n:b}"
    i = b.rfind("01")
    return int(f"{b[:i]}10{''.join(sorted(b[i+2:]))}", 2)
