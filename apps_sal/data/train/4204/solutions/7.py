def findR(num):
    while True:
        if str(num) == str(num)[::-1]:
            return num
        num += 1


def findL(num):
    while True:
        if str(num) == str(num)[::-1]:
            return num
        num -= 1


def palindrome(num):
    if type(num) != int or num < 0:
        return 'Not valid'
    if num <= 10:
        return 11
    elif findR(num) - num <= num - findL(num):
        return findR(num)
    else:
        return findL(num)
