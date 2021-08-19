def sorter(textbooks):
    # Cramming before a test can't be that bad?
    #     return sorted(textbooks, key=cmp_to_key(locale.strcoll))
    textbooks.sort(key=str.lower)
    return textbooks
