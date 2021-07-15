def longest_palindrome (s):
    if not s: return 0
    substrings = [s[i:j] for i in range(0,len(s)) for j in range(i,len(s)+1)]
    return max(len(s) for s in substrings if s == s[::-1])
