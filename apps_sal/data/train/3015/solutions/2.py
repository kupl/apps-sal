import re
REGEX = re.compile('\n(?P<AMEX>3[47]\\d{13}$) |\n(?P<Discover>6011\\d{12}$) |\n(?P<Mastercard>5[1-5]\\d{14}$) |\n(?P<VISA>(?:4\\d{15}|4\\d{12})$)', re.VERBOSE)


def get_issuer(card_num):
    try:
        return next((k for (k, v) in REGEX.match(str(card_num)).groupdict().items() if v is not None))
    except AttributeError:
        return 'Unknown'
