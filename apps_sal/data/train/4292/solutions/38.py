import re


def string_clean(string): return re.sub('\d', '', string)

"""remove all digits from the string"""
