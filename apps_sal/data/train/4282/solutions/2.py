import re
hungry_seven = lambda arr: (lambda h: lambda x: h(h, x))(lambda h, x: h(h, re.sub(r'(7+)(89)', r'\2\1', x)) if re.search(r'(7+)(89)', x) else [int(c) for c in x])(''.join(map(str, arr)))

