def palindrome(num):
    if type(123) != type(num):
        return 'Not valid'
    n = str(num)
    if any((not c.isdigit() for c in n)):
        return 'Not valid'
    l = len(n)
    return all((a == b for (a, b) in zip(n[:l // 2], n[::-1])))
