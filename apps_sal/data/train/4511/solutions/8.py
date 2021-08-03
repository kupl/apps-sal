def permute_a_palindrome(string):
    even = 0
    odd = 0
    letters = list()
    for elem in string:
        if elem not in letters:
            letters.append(elem)
            if string.count(elem) % 2 == 0:
                even += 1
            else:
                odd += 1
    if (len(string) % 2 != 0 and odd == 1) or (len(string) % 2 == 0 and odd == 0):
        return True
    return False
