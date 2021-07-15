def sorter(textbooks):
    copy = [text.lower() for text in textbooks]
    final = []
    to_sort = list(copy)
    to_sort.sort()
    for t in to_sort:
        final.append(textbooks[copy.index(t)])
    return final
