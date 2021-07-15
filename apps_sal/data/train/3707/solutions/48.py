def sorter(*textbooks):
    for textbook in textbooks:
        print(textbook.sort(key=str.lower))
    return textbook
