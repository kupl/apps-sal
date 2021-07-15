def longest_palindrome (s):
    return max((n for n in range(len(s), 0, -1) for i in range(len(s)-n+1) if s[i:i+n] == s[i:i+n][::-1]), default=0)
