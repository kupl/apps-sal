def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    s = str(num)
    return sum(sum(s[i:i + n] == s[i:i + n][::-1] for i in range(len(s) - n + 1)) for n in range(2, len(s) + 1))
