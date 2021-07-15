def cal(s):
    if not s : return 0
    if not s.isalpha() : return 0
    return sum([ord(x) for x in s.upper()])

def compare(s1,s2):
    return cal(s1)==cal(s2)
