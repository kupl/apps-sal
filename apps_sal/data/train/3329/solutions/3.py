def longest_palindrome(s):
    if s:
        return max(map(len, filter(palindrome, substrings(s))))
    else:
        return 0


def palindrome(s):
    return s[::-1] == s


def substrings(s):
    return [s[i:j + 1] for i in range(0, len(s)) for j in range(i, len(s))]
