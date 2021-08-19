import re


def reverse_words(text):
    li_text = re.split("( )", text)  # Why must regular split be different from regex split :/
    solution = ''.join(list(word[::-1] for word in li_text))  # Separated from split for readability.

    return solution
