import string
def lowercase_count(s):
    return sum([1 for i in s if i in string.ascii_lowercase])
