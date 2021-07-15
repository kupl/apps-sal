def kooka_counter(laughing):
    if len(laughing) == 0:
        return 0
    return laughing.count('haHa') + laughing.count('Haha') + 1
