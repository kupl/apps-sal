def evil(n):
    return f"It's {'Odious' if '{0:b}'.format(n).count('1')%2 else 'Evil'}!"
