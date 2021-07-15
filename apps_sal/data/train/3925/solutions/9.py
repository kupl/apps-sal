def is_john_lying(a,b,s):
    return (a+b)%2==s%2 and abs(a)+abs(b)<=s
