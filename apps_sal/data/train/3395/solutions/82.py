def remove_duplicate_words(s):
    list = s.split()
    index = 0
    empty = []
    while index < len(list):
        if list[index] not in list[0:index]:
            empty.append(list[index])
        index += 1
    return ' '.join(empty)
