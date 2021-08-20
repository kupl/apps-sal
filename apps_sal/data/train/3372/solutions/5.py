def string_merge(string1, string2, letter):
    return f'{string1.partition(letter)[0]}{letter}{string2.partition(letter)[-1]}'
