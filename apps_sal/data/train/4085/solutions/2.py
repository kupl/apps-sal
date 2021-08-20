import random
import re
import numpy as np


def mix_words(text):
    words_list = text.split()
    result_list = []
    for word in words_list:
        punctuation = ''.join(re.findall('\\W', word))
        text_list = [x for x in word]
        blank_list = ['' for x in range(len(word))]
        lst = [x for x in range(1, len(text_list) - (len(punctuation) + 1))]
        lst2 = lst[:]
        if len(lst) > 1:
            while np.array_equal(lst, lst2):
                random.shuffle(lst2)
            j = 0
            for i in range(len(word)):
                if i == 0:
                    blank_list[i] = text_list[i]
                elif len(punctuation) > 0 and (text_list[i] in punctuation or text_list[i + 1] in punctuation):
                    blank_list[i] = text_list[i]
                elif len(punctuation) == 0 and i == len(word) - 1:
                    blank_list[i] = text_list[i]
                else:
                    blank_list[i] = text_list[lst2[j]]
                    j += 1
            new_text = ''.join(blank_list)
            result_list.append(new_text)
        else:
            result_list.append(word)
    result = ''.join([item + ' ' for item in result_list]).strip()
    if (len(lst) > 2) & (result == text):
        result = mix_words(text)
    return result
