'''
    Write a function that returns the longest contiguous palindromic substring in s. 
    In the event that there are multiple longest palindromic substrings, return the 
    first to occur.
'''


def longest_palindrome(s, sep=" "):
    # Interpolate some inert character between input characters
    # so we only have to find odd-length palindromes
    t = sep + sep.join(s) + sep

    r = 0       # Rightmost index in any palindrome found so far ...
    c = 0       # ... and the index of the centre of that palindrome.
    spans = []  # Length of the longest substring in T[i:] mirrored in T[i::-1]

    # Manacher's algorithm
    for i, _ in enumerate(t):
        span = min(spans[2 * c - i], r - i - 1) if i < r else 0
        while span <= i < len(t) - span and t[i - span] == t[i + span]:
            span += 1
        r, c = max((r, c), (i + span, i))
        spans.append(span)

    span = max(spans)
    middle = spans.index(span)

    return t[middle - span + 1:middle + span].replace(sep, "")
