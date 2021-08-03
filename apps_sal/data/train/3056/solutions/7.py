def palindrome(num, s):

    def ispali(n): return str(n) == str(n)[::-1]

    if not isinstance(num, int) or num < 0 or not isinstance(s, int) or s < 0:
        return "Not valid"

    i = max(num, 10)
    ans = []
    while len(ans) < s:
        if ispali(i):
            ans.append(i)
        i += 1
    return ans
