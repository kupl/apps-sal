def compare(s1,s2):
    s1=s1 if (s1 and s1.isalpha()) else ""
    s2=s2 if (s2 and s2.isalpha()) else ""
    
    return sum(map(ord,s1.upper()))==sum(map(ord,s2.upper()))

