def solve(s):
    return sum( int(c)%2 for i in range(len(s)) for c in s[i:] )
