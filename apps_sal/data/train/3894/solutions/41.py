import string
def solve(s):
    return s.lower() if [(l in string.ascii_lowercase) for l in s].count(True)>=len(s)//2 else s.upper()
