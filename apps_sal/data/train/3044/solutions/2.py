def solve(s):
    for i in range(len(s)):
        if s == s[::-1]:
            return True

        s = s[1:] + s[0]

    return False
