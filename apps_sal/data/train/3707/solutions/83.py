def sorter(textbooks):
    sorted = [book.lower() for book in textbooks]
    sorted.sort()
    final = textbooks.copy()
    for book in textbooks:
        final[sorted.index(book.lower())] = book
    return final
