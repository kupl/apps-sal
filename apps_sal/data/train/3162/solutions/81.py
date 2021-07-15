def av(s):
    if not s: return 0
    if s.isalpha():
        return sum(ord(i) for i in s.upper())
    return 0
def compare(s1,s2):
    return av(s1)==av(s2)
