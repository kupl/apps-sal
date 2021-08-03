def cooking_time(n, m, s, p): return '{} minutes {} seconds'.format(*divmod(-(-(m * 60 + s) * int(n[:-1]) // int(p[:-1])), 60))
