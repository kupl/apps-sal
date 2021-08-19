def is_palindrome(s):
    s = s.lower()
    orden1 = list(s)
    orden2 = orden1[::-1]
    if orden1 == orden2:
        bool = True
    else:
        bool = False
    return bool
