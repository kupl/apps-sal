def six_column_encryption(msg):
    msg = msg.replace(' ', '.') + '.' * ((6 - len(msg) % 6) % 6)
    return ' '.join((msg[n::6] for n in range(6)))
