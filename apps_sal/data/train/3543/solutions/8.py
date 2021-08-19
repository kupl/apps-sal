increment_string = f = lambda s: s and s[-1].isdigit() and (f(s[:-1]) + '0', s[:-1] + str(int(s[-1]) + 1))[s[-1] < '9'] or s + '1'
