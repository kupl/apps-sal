def solve(s):
    for i in range(len(s)):
        xs = s[i:] + s[:i]
        if xs == xs[::-1]:
            return True
    return False

