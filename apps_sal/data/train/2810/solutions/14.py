import string


def solve(arr):
    corrects = []
    for word in arr:
        correct_place = 0
        for index, char in enumerate(word):
            alph_index = string.ascii_lowercase.find(char.lower())
            if index == alph_index:
                correct_place = correct_place + 1
        corrects.append(correct_place)
    return corrects
