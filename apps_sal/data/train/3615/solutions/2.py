from operator import itemgetter
from collections import Counter
from itertools import chain


def presentation_agenda(friend_list):
    okay = {k for k, v in Counter(chain.from_iterable(map(itemgetter('dest'), friend_list))).items() if v == 1}.__contains__
    result = []
    for friend in friend_list:
        temp = list(filter(okay, friend['dest']))
        if temp:
            result.append({'person': friend['person'], 'dest': temp})
    return result
