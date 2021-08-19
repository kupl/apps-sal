def solve(s):

    def isOK(x):
        return x == x[::-1]
    return 'OK' if isOK(s) else 'remove one' if any((isOK(s[:i] + s[i + 1:]) for i in range(len(s)))) else 'not possible'
