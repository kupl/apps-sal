def is_pali(num):
    return str(num) == str(num)[::-1] and num > 9


def palindrome(num):
    if type(num) != int or str(num) != str(int(num)) or int(num) < 0:
        return 'Not valid'
    n = 0
    if num <= 11:
        return 11
    while n < num:
        test1 = num - n
        test2 = num + n
        if is_pali(test2):
            return num + n
        elif is_pali(test1):
            return num - n
        n += 1
