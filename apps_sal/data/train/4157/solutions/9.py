def group_check(s):
    for e in ['()','{}','[]','{}','()']:
        while e in s: s = s.replace(e,'')
    return not s
