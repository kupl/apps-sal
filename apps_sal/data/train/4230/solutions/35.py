import re


def reverse_letter(st):
    newst = st[::-1]
    itog = ""
    for i in newst:
        if i.isalpha():
            itog += i
    return (itog)
