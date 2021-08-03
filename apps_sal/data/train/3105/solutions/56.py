def count_sheep(n):
    str = ""
    x = 1
    while x <= n:
        str += (f"{x} sheep...")
        x += 1
    return (str)
