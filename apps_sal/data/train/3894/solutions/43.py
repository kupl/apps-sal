def solve(s):
    return s.upper() if sum([1 for x in s if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])>len(s)/2 else s.lower()
