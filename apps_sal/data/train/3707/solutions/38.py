def sorter(textbooks):
    #Cramming before a test can't be that bad?
    bookList = sorted(textbooks, key=str.lower)
    return bookList
