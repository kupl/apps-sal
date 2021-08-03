from collections import Counter


def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    return True if num > 10 and 1 >= sum(map(lambda oc: oc % 2, Counter(str(num)).values())) else False
