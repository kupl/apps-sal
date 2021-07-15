from operator import itemgetter

def read_out(acrostic):
    return ''.join(map(itemgetter(0), acrostic))
