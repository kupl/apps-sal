def uni_total(string):
    array = []
    copy = []
    array = list(string)
    for num in array:
        copy.append(ord(num))
    total = sum(copy)
    return total
