import re


def get_issuer(number):
    p = re.compile('^(?P<VISA>4(\\d{15}|\\d{12})$)|(?P<AMEX>^(34|37)\\d{13}$)|(?P<Mastercard>5[1-5]\\d{14}$)|(?P<Discover>6011\\d{12}$)').match(str(number))
    return [k for (k, v) in p.groupdict().items() if v][0] if p else 'Unknown'
