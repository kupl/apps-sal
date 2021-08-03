import re


def validPhoneNumber(num):
    return bool(re.match("^[(][0-9]{3}[)] [0-9]{3}-[0-9]{4}$", num))
