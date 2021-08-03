import re


def timed_reading(max_length, text):
    text = re.sub(r'[^\w\s]', '', text)
    cnt = 0
    for words in text.split():
        if len(words) <= max_length:
            cnt += 1

    return cnt
