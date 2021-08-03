def compare(s1, s2):
    if s1 == None or [e for e in s1.lower() if not 'a' <= e <= 'z']:
        s1 = ""
    if s2 == None or [e for e in s2.lower() if not 'a' <= e <= 'z']:
        s2 = ""
    if sorted(s1.lower()) == sorted(s2.lower()):
        return True
    return sum([ord(e) for e in s1]) == sum([ord(e) for e in s2])
