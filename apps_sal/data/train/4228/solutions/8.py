def palindrome(n):
    if not isinstance(n, int) or n < 0:
        return "Not valid"
    s = str(n)
    return sum(s[i:j] == s[i:j][::-1]
               for i in range(len(s) - 1)
               for j in range(i + 2, len(s) + 1))
