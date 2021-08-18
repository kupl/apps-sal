import re


def reverse_words(text):
    li_text = re.split("( )", text)
    solution = ''.join(list(word[::-1] for word in li_text))

    return solution
