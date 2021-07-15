from collections import Counter
def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    return num > 10 and sum(1 for v in Counter(map(int, str(num))).values() if v % 2) <= 1
