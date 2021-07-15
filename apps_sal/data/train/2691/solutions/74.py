def solve(s):
     return max([int(s) for s in "".join([c if '9'>=c>='0' else ' ' for c in s]).split()])
