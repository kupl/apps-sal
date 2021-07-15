def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return "Not valid"
    s = str(num)
    l = len(s)
    return sum(1 for p in (s[i:i+1+j] for j in range(1, l) for i in range(l-j)) if p == p[::-1])
