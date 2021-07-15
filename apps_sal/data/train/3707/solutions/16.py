def sorter(textbooks: list) -> list:
    return sorted(textbooks, key=str.casefold)
