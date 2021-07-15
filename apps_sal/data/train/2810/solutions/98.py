import string

def solve(arr):
    alphabet_indexes = list(enumerate(string.ascii_lowercase))
    letters_count = []
    for word in arr:
        num_of_letters = 0
        letters_indexes = list(enumerate(word.lower()))
        if len(word) > len(alphabet_indexes):
            word = word[:26]
        for i in range(len(word)):
            if letters_indexes[i] == alphabet_indexes[i]:
                num_of_letters += 1
        letters_count.append(num_of_letters)
    return letters_count
