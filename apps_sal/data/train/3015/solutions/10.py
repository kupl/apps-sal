import re


def get_issuer(number):
    for n, r in ('AMEX', '3[47].{13}'), ('Discover', '6011.{12}'), ('Mastercard', '5[1-5].{14}'), ('VISA', '4(...){4,5}'):
        if re.fullmatch(r, str(number)):
            return n
    return 'Unknown'
