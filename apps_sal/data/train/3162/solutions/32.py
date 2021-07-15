import re
def compare(s1,s2):
    def sums(s):
        return '' if(not s or re.search('[^A-Za-z]', s)) else sum(ord(x) for x in s.upper())
    return sums(s1) == sums(s2)
