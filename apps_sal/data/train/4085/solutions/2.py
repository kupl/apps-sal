import random
import re
import numpy as np


def mix_words(text):
    words_list = text.split()
    result_list = []

    for word in words_list:
        punctuation = ''.join(re.findall("\W", word))
        # punctuation = ''.join(re.findall("[^a-zA-Z]", word))  #equivalent to line above, get non-alphanumeric characters

        # create 2 lists, the 1st as the word split into a list, the 2nd an empty list of the same size that will
        # be get filled in sequentially
        text_list = [x for x in word]
        blank_list = ['' for x in range(len(word))]

        # need to isolate the middle part of the word (not 1st, last, punctuation)
        # assumption that any punctuation is at the end of each word. e.g. hello!, not hel?lo
        lst = [x for x in range(1, (len(text_list) - (len(punctuation) + 1)))]
        lst2 = lst[:]

        # if there is only 1 randmisable character its position can't be changed
        if len(lst) > 1:
            # shuffle the order of the randomisable characters, shuffle could return the same order (by chance) so perform
            # this operation inside a while loop
            while (np.array_equal(lst, lst2)):
                random.shuffle(lst2)

            # j variable is a counter for which element to take from the randomised characters list
            j = 0
            for i in range(len(word)):
                if i == 0:
                    # Keep first character in position
                    blank_list[i] = text_list[i]
                elif (len(punctuation) > 0) and ((text_list[i] in punctuation) or (text_list[i + 1] in punctuation)):
                    # Keep punctuation and last character (if there's punctuation) in position
                    blank_list[i] = text_list[i]
                elif (len(punctuation) == 0) and (i == len(word) - 1):
                    # Keep last character in position, if no punctuation
                    blank_list[i] = text_list[i]
                else:
                    # if the character is not punctuation or first/last character then take from the randomised list
                    blank_list[i] = text_list[lst2[j]]
                    j += 1

            new_text = ''.join(blank_list)
            # join the individual list elements for each word together to create the randomised word
            result_list.append(new_text)
            # append the
        else:
            # if the word is less than 3 characters return the original word
            result_list.append(word)
    result = ''.join([item + ' ' for item in result_list]).strip()

    if (len(lst) > 2) & (result == text):
        result = mix_words(text)

    return result
