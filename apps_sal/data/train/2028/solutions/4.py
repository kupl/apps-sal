def isPalindrom(s, n):
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True


def solve(s):
    if len(s) % 2 == 0:
        temp = s[0] * len(s)
        if s == temp:
            return 'Impossible'
    elif len(s) == 1:
        return 'Impossible'
    else:
        c = s[0]
        mid = s[len(s) // 2]
        temp = c * (len(s) // 2) + mid + c * (len(s) // 2)
        if temp == s:
            return 'Impossible'
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            temp = s[i:] + s[:i]
            if temp != s and isPalindrom(temp, n):
                return 1
    return 2


s = input()
print(solve(s))
