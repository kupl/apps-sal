def solve(s):
    if s == s[::-1]:
        return 'OK'
    s = [letter for letter in s]
    k = [letter for letter in s]
    for char in range(len(s)):
        s.pop(char)
        s = ''.join(s)
        if s == s[::-1]:
            return 'remove one'
        s = [letter for letter in k]
    return 'not possible'
