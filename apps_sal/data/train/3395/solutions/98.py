def remove_duplicate_words(str):
    return ' '.join(sorted(set(str.split()), key=str.split().index))
