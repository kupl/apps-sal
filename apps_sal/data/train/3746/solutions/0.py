def palindrome(n):
    s = str(n)
    return s[::-1] == s

def next_pal(val):
    val += 1
    while not palindrome(val):
        val += 1
    return val
