def number_format(n): return ''.join(',' * (i % 3 == 0) + x for i, x in enumerate(str(n)[::-1]))[::-1].replace('-,', '-').strip(',')
