from numpy import prod


def find_middle(string):
    return int(findMiddle(str(prod(list(map(int, filter(type(string).isdigit, string))))))) if type(string) is str and any((char.isdigit() for char in string)) else -1


def findMiddle(s):
    return s[int(len(s) / 2) - 1:int(len(s) / 2) + 1] if not len(s) % 2 else s[int(len(s) / 2):int(len(s) / 2) + 1]
