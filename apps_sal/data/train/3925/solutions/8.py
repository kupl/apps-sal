def is_john_lying(a,b,s):
    c = abs(a)+abs(b)
    return c%2==s%2 and c<=s
