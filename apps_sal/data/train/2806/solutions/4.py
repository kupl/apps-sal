import re


def whose_turn(positions):
    return len(re.sub('[1357;aceg]', '', positions)) % 2 == 0
