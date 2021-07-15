def number(lines):
    count,dictionary = 1,{}
    for element in lines:
        dictionary[count] = element
        count += 1
    return [(str(key) + ": " + str(value)) for key,value in list(dictionary.items())]

