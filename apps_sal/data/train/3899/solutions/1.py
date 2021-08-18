from re import sub


def guess_my_number(guess, number='123-451-2345'):
    return sub('[^{}-]'.format(guess), '
