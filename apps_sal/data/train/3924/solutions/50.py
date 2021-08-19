import re


def reverse_words(text):
  # go for it
    # split the string by spaces
    arr = re.split(r'(\s+)', text)
    # see the array
    # for loop to reverse each string within the array
    reverse = [i[::-1]for i in arr]
    finished = ''.join(reverse)
    return finished
