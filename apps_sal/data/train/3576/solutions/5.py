def longest(words):
    number = [len(i) for i in words]
    number.sort()
    length = number.pop()
    return length
