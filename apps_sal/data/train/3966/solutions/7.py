def solution(full_text, search_text):
    return full_text.replace(search_text, '1').count('1')
