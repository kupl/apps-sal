import string

def lowercase_count(strng):
    count = 0
    for str in strng:
        if str in string.ascii_lowercase:
            count += 1
    return count
