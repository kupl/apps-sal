import re
f = remove_parentheses = lambda s: f(re.sub('\\([^\\(\\)]*\\)', '', s)) if '(' in s else s
