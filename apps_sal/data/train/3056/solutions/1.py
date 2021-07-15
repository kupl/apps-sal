def palindrome(num, s):
    if not isinstance(num, int) or not isinstance(s, int) or num < 0 or s < 0:
        return 'Not valid'
    lst = []
    while len(lst) < s:
        if str(num) == str(num)[::-1] and num > 9:
            lst.append(num)
        num += 1
    return lst
