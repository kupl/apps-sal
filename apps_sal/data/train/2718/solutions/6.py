def timed_reading(max_l, text):
    string = text.translate(str.maketrans('`~!@\'\"#№$;%:^&?*()-_+=/\[]{}', '                            '))
    return sum(map(lambda x: len(x) <= max_l, (i for i in string.split() if i)))
