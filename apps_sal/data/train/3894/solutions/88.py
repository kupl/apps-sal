import string
def solve(s):
    sum = 0
    for i in range(len(s)):
        if s[i] in string.ascii_lowercase:
            sum+=1
    return s.lower() if sum>= len(s)/2 else s.upper()
