def six_column_encryption(s): return ' '.join(map(''.join, zip(*zip(*[iter(s.replace(' ', '.') + '.' * 5)] * 6))))
