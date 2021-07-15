def inrange(a,b,x):
    if x>=a and x<=b:
        return True
    else:
        return False
def make_upper_case(s):
    ans=""
    for x in s:
        if inrange(ord('a'),ord('z'),ord(x)):
            x=chr(ord('A')+(ord(x)-ord('a')))
        ans=ans+x
    return ans
