from re import search, sub, findall
count_me = lambda s: '' if search('[^0-9]', s) != None else sub('(.)\\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
