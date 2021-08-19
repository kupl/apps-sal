import string
import numpy as np
alpha = list(string.ascii_lowercase)
values = list(range(1, 27))
dictionary = dict(zip(alpha, values))


def encode(word, old_key):
    key = [int(x) for x in str(old_key)]
    letter_values = []
    for letter in word:
        letter_values.append(dictionary[letter])
    count = 0
    new_list = []
    while count < len(word):
        for number in key:
            if count >= len(word):
                break
            else:
                count += 1
                new_list.append(number)
    key_np = np.array(new_list)
    letter_np = np.array(letter_values)
    final = (key_np + letter_np).tolist()
    return final
