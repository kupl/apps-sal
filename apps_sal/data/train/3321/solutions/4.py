def evil(n):
    return f"It's {('Evil', 'Odious')[bin(n).count('1') & 1]}!"
