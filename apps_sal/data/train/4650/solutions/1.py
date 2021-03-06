import re
prog = re.compile('^\\(\\d{3}\\) \\d{3}-\\d{4}$')


def validPhoneNumber(phone_number):
    return prog.match(phone_number) is not None
