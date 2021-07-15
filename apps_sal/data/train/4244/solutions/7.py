from collections import Counter

def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    occ2 = [0, 0]
    for freq in Counter(str(num)).values():
        occ2[freq % 2] += freq % 2
    return num >= 10 and occ2[1] <= 1
