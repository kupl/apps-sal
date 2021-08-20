import re


def solution(full_text, search_text):
    return len(re.findall('{}'.format(search_text), full_text))
