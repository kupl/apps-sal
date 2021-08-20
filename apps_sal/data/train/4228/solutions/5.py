def palindrome(num):
    cnt = 0
    if type(num) != int or num < 0:
        return 'Not valid'
    s = str(num)
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                cnt += 1
    return cnt
