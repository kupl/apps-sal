insert_dash2 = lambda n, r=__import__('re').sub, a='2468', b='13579': r(f'([{a}])(?=[{a}])', '\\1*', r(f'([{b}])(?=[{b}])', '\\1-', str(n)))
