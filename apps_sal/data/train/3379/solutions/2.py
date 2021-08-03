def encrypter(strng):
    z = {0: 'm', 1: 'l', 2: 'k', 3: 'j', 4: 'i', 5: 'h', 6: 'g', 7: 'f', 8: 'e', 9: 'd', 10: 'c', 11: 'b', 12: 'a', 13: 'z', 14: 'y', 15: 'x', 16: 'w', 17: 'v', 18: 'u', 19: 't', 20: 's', 21: 'r', 22: 'q', 23: 'p', 24: 'o', 25: 'n'}
    pt = ''
    for i in strng:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            pt += z[ord(i) - ord('a')]
        else:
            pt = pt + i
    return pt  # your code here
