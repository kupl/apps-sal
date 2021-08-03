from collections import Counter


def get_strings(word):
    return ','.join(
        f'{letter}:{"*" * count}'
        for letter, count in Counter(word.lower()).items()
        if letter.isalpha())
