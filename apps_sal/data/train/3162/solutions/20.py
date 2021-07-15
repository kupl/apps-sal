def compare(s1,s2):
    n1=n2=0
    if s1 and all(i.isalpha() for i in s1):
        n1=sum(ord(i) for i in s1.upper())
    if s2 and all(i.isalpha() for i in s2):
        n2=sum(ord(i) for i in s2.upper())
    return n1==n2
