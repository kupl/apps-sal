six_column_encryption=lambda s:' '.join(map(''.join,zip(*zip(*[iter(s.replace(' ','.')+'.'*5)]*6))))
