def solution(full_text, search_text):
    c = 0
    for i in range(len(full_text) - len(search_text) + 1):
        if full_text[i:i + len(search_text)] == search_text:
            c += 1
    return c
