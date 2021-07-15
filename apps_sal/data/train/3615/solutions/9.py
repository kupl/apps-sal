from collections import Counter

def presentation_agenda(friend_list):
    all_dests = sum((friend['dest'] for friend in friend_list), [])
    uniq_dests = [dest for dest, count in Counter(all_dests).items() if count == 1]
    agenda = []
    for friend in friend_list:
        uniq = [x for x in friend['dest'] if x in uniq_dests]
        if uniq:
            agenda.append({'person': friend['person'], 'dest': uniq})
    return agenda
