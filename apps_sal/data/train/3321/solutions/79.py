def evil(n):
    verdict = 'Odious' if bin(n).count('1') % 2 else 'Evil'
    return f"It's {verdict}!"
