from datetime import datetime

def to24hourtime(h, m, p):
    return datetime.strptime('%02d%02d%s' % (h, m, p.upper()), '%I%M%p').strftime('%H%M')
