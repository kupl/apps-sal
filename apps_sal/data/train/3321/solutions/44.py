def evil(n): return "It's " + ('Odious!' if str(bin(n)).count('1') & 1 else 'Evil!')
