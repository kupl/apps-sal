def sorter(textbooks):
    sorted_books = sorted(textbooks, key=str.casefold)

    return sorted_books
