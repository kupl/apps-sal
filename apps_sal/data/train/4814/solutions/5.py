def is_palindrome(s):

    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:

        if s[p1].lower() == s[p2].lower():
            p1 += 1
            p2 -= 1
            continue

        else:
            return False

    return True
