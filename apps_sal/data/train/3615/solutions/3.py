def presentation_agenda(friend_list):
    result = []
    for (i, friend) in enumerate(friend_list):
        ds = {x for (j, f) in enumerate(friend_list) if j != i for x in f['dest']}
        xs = [x for x in friend['dest'] if x not in ds]
        if xs:
            result.append({'person': friend['person'], 'dest': xs})
    return result
