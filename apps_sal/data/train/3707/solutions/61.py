def sorter(textbooks):
    if textbooks!=int:
        return sorted(textbooks,key=str.lower)
