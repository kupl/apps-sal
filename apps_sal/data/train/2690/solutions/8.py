import re
f = remove_parentheses = lambda s: f(re.sub(r'\([^\(\)]*\)', '', s))if'(' in s else s
