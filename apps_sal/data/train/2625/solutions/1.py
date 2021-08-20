import re
num = input()
print(bool(re.match('^[1-9][\\d]{5}$', num) and len(re.findall('(\\d)(?=\\d\\1)', num)) < 2))
