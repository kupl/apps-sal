def only_duplicates(string):
    string = list(string)
    foundStrings = []
    finalString = []
    for (index, item) in enumerate(string):
        if item not in string[index + 1:len(string)] and item not in string[0:index]:
            finalString.append('')
        else:
            finalString.append(item)
    return ''.join(finalString)
