import re

issuers = (
    ('AMEX', '3[47].{13}'),
    ('Discover', '6011.{12}'),
    ('Mastercard', '5[1-5].{14}'),
    ('VISA', '4(...){4,5}'),
    ('Unknown', '.*')
)


def get_issuer(number):
    return next(name for name, regex in issuers if re.fullmatch(regex, str(number)))
