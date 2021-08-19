def evil(n):
    str = bin(n)
    total = sum((a == '1' for a in str))
    return "It's Odious!" if total % 2 != 0 else "It's Evil!"
