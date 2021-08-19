from re import *


def short_form(s):
    return sub('(?<!^)[aeiou](?=.)', '', s, flags=I)
