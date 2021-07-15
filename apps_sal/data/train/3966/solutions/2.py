import re
def solution(full_text, search_text):
    return len(re.findall(r'(' + search_text + ')', full_text))
