import re
from itertools import groupby
CONFIG = {'FURY': ' really', 'FIRE': ' and you', 'FAKE': 'Fake tweet.', 'FURY_f': 'I am{} furious.', 'FIRE_f': 'You{} are fired!'}


def fire_and_fury(tweet):
    if re.findall('[^FURYIE]', tweet):
        return CONFIG['FAKE']
    lst = []
    for (k, g) in groupby(re.findall('FURY|FIRE', tweet)):
        lst += [CONFIG[k + '_f'].format(CONFIG[k] * (len(list(g)) - 1))]
    return ' '.join(lst) or CONFIG['FAKE']
