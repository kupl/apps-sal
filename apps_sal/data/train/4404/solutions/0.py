def compare(s1, s2):
    v1,v2 = version(s1),version(s2)
    return -1 if v1 < v2 else 1 if v1 > v2 else 0

def version( s ):
    v = [int(n) for n in s.split(".")]
    while( v[-1]==0 ) : v = v[0:-1]
    return v
