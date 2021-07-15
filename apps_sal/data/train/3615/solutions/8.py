def presentation_agenda(friend_list):
    out = []
    for friend in friend_list:
        p_list = friend['dest']
        sub_list = [x for x in friend_list if x != friend]
        for f in sub_list:
            p_list = [loc for loc in p_list if loc not in f['dest']]
        if len(p_list):
            out.append({'person': friend['person'], 'dest': p_list})
    return out

