from collections import Counter


def presentation_agenda(friend_list):
    uniqueDest = {d for d, c in Counter(d for p in friend_list for d in p['dest']).items() if c == 1}
    pFilteredDest = tuple((p['person'], [d for d in p['dest'] if d in uniqueDest]) for p in friend_list)
    return [{'person': name, 'dest': lst} for name, lst in pFilteredDest if lst]
