VENDORS = [
    ['AMEX', (34, 37), (15,)],
    ['Discover', (6011,), (16,)],
    ['Mastercard', range(51, 56), (16,)],
    ['VISA', (4,), (13, 16)],
]


def get_issuer(number):
    return next((
        vendor[0] for vendor in VENDORS
        if len(str(number)) in vendor[2] and any(str(number).startswith(str(start)) for start in vendor[1])
    ), 'Unknown')
