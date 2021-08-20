import itertools
import re
MEANINGS = {'FIRE': [lambda i: 'You are fired!', lambda i: f"You{' and you' * i} are fired!"], 'FURY': [lambda i: 'I am furious.', lambda i: f"I am{' really' * i} furious."]}


def fire_and_fury(tweet):
    if re.search('[^EFIRUY]', tweet):
        tweet = ''
    return ' '.join((MEANINGS[key][n > 1](n - 1) for (key, grp) in itertools.groupby(re.findall('FIRE|FURY', tweet)) for n in [sum((1 for _ in grp))])) or 'Fake tweet.'
