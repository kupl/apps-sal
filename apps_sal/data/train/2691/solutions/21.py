def solve(s):
    return max(map(int, [c for c in ''.join([v if not v.isalpha() else '|' for v in s]).split('|') if c != '']))
