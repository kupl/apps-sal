import re


def reverse_letter(string):
    return re.sub(r"""[0-9!@#$%^&*?/ \/(/)/{/}/+/-/*/[/\]/~/`/./,/>/</'/"/?\=\\:_|\-;]""", "", string)[::-1]
