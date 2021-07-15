def solve(s):
    s = s.replace('a',' ').replace('e',' ').replace('i',' ').replace('u',' ').replace('o',' ')
    return max((sum(ord(i)-96 for i in j) for j in s.split()))
