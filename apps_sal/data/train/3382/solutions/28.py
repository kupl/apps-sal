def lowercase_count(s):
    return sum((1 for i in s if 'a' <= i <= 'z'))
