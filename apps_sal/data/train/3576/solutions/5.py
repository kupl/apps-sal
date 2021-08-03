def longest(words):
    # Your code here
    number = [len(i) for i in words]
    number.sort()
    length = number.pop()
    return length
