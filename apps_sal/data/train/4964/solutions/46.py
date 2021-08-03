import copy


def is_uppercase(inp):
    return inp == copy.copy(inp).upper()
