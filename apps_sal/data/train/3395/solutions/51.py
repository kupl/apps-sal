def remove_duplicate_words(x):
    y = []
    for i in x.split():
        if i in y:
            pass
        else:
            y.append(i)
    return ' '.join(y)
