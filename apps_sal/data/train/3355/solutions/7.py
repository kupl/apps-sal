import re
def difference(n,s) :
    n = str(n)[::-1]
    try :
        right_index = n.index(s[1])
        left_index = n.index(s[0],[0,1 + right_index][s[0] == s[1]])
    except : return float('inf')
    upper_index = 1 + max(left_index,right_index) == len(n) and '0' == n[-2] and len(re.search('0*.$',n)[0])
    return right_index + left_index - 1 + (left_index < right_index) + (upper_index and upper_index - 1 - (len(n) <= min(left_index,right_index) + upper_index))
def solve(n) :
    removes = min([difference(n,'00'),difference(n,'25'),difference(n,'50'),difference(n,'75')])
    return [-1,removes][int == type(removes)]

