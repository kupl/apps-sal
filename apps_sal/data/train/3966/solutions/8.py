import re


def solution(full_text, search_text):
    res = re.findall(search_text, full_text)
    return len(res)
