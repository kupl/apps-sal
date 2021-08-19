from collections import Counter


def get_strings(city):
    myList = []
    counter = Counter(city.lower())
    for letter in counter:
        if letter == ' ':
            pass
        else:
            myList.append(letter + ':' + str('*' * city.lower().count(letter)))
    return ','.join(myList)
