import re


def reverse_letter(string):
    return re.sub('[0-9!@#$%^&*?/ \\/(/)/{/}/+/-/*/[/\\]/~/`/./,/>/</\'/"/?\\=\\\\:_|\\-;]', '', string)[::-1]
