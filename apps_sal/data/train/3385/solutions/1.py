def longest(string):
    start = 0
    longest = string[0:1]
    length = len(string)
    for i in range(1, length):
        if string[i] < string[i - 1] or i == length - 1:
            if string[i] < string[i - 1]:
                last = string[start:i]
                start = i
            else:
                last = string[start:]
            if len(last) > len(longest):
                longest = last
    return longest
