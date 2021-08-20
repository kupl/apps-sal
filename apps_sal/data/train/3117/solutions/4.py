def solve(s):
    return max((len(w) for w in ''.join(([' ', c][c in 'aeiou'] for c in s)).split()))
