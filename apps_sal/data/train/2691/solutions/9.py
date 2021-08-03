import re
P = re.compile('\d+')
def solve(s): return max(map(int, (P.findall(s))))
