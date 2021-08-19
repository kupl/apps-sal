def no_ifs_no_buts(a, b):
    return '{} is {} {}'.format(a, ['{}er than'.format(['great', 'small'][a < b]), 'equal to'][a == b], b)
