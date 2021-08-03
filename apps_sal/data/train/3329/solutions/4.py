def longest_palindrome(s):

    longest = 0

    for j in range(1, len(s) + 1):
        for i in range(j):
            t = s[i:j]
            if t == t[::-1]:
                longest = max(longest, len(t))

    return longest
