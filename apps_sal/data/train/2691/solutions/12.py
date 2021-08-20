def solve(s):
    return max(map(int, ''.join((c if c in '0123456789' else ' ' for c in s)).split()))
