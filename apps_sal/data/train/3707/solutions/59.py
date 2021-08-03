def sorter(textbooks):
    lst_books = []
    for i in textbooks:
        lst_books.append(i)
    return sorted(lst_books, key=str.lower)
