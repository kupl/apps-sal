def is_palindrome(string):

    target = str(string)
    start, end = 0, len(target) - 1
    while (start < end):
        if (target[start] != target[end]):

            return False

        start += 1
        end -= 1

    return True
