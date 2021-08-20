import re
from itertools import groupby


def fire_and_fury(tweet):
    text = ' '.join(('I am{} furious.'.format(' really' * ~-len(list(g))) if k == 'FURY' else 'You{} are fired!'.format(' and you' * ~-len(list(g))) for (k, g) in groupby(re.findall('FIRE|FURY', tweet))))
    return text if re.fullmatch('[EFIRUY]+', tweet) and text else 'Fake tweet.'
