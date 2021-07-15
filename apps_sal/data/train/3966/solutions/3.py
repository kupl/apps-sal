def solution(full_text, search_text):
    count = 0
    length = len(search_text)
    for i in range(len(full_text)-length + 1):
        if full_text[i : i+length] == search_text:
            count += 1
    return count

