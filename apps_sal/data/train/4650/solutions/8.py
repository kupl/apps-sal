def validPhoneNumber(s):
    if s.count(' ') == s.count('-') == 1 and len(s) == 14:
        a = s.replace('(','').replace(')','').replace('-',' ')
        b = a.split()
        return [len(x) for x in b] == [3,3,4]
    return False
