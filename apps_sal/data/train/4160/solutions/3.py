from operator import truediv


def get_percentage(sent, limit=1000):
    if not sent:
        return 'No e-mails sent'
    elif sent >= limit:
        return 'Daily limit is reached'
    return '{}%'.format(int(truediv(sent, limit) * 100))
