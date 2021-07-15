import string
def lowercase_count(strng):
    return sum([x in string.ascii_lowercase for x in strng])
