def evil(n):
    return f"It's {['Odious', 'Evil'][bin(n).count('1') % 2 == 0]}!"
