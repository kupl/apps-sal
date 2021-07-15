import re
P = re.compile('\d+')
solve = lambda s: max(map(int, (P.findall(s))))
