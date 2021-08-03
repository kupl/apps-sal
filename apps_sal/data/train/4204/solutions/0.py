def palindrome(num):
    if type(num) is not int or num < 0:
        return "Not valid"
    else:
        c = 0
        for i in range(num, num**2):
            if is_pal(i):
                return i
            elif is_pal(i - c):
                return i - c
            else:
                c += 2


def is_pal(n):
    return n > 10 and n == int(str(n)[::-1])
