import functools
def reverse_words(text):
    reversed_text = list(functools.reduce(
        lambda acc,st: acc + st, [''.join(reversed(word)) for word in text.split()], ''))
    return_arr = []
    for ch in text:
        if ch.isspace():
            return_arr.append(" ")
        else:
            return_arr.append(reversed_text.pop(0))
    return ''.join(return_arr)

