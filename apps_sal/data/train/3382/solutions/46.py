def lowercase_count(strng):
    count = 0
    for letter in strng:
        if letter.isalpha():
            if ord(letter) <= ord('z') and ord(letter) >= ord('a'):
                count += 1
    return count
