def get_percentage(s, l=1000):
    return 'No e-mails sent' * (s < 1) or '%d%%' % (100 * s // l) * (s < l) or 'Daily limit is reached'
