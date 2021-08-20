def fight(A, B, damage):
    if B['speed'] > A['speed']:
        (A, B) = (B, A)
    while A['tactics'] or B['tactics']:
        for (attack, defend) in [(A, B), (B, A)]:
            if attack['tactics']:
                defend['health'] -= damage[attack['tactics'][0]]
                attack['tactics'] = attack['tactics'][1:]
                if defend['health'] <= 0:
                    return attack['name'] + ' has won the fight.'
    return 'The fight was a draw.' if A['health'] == B['health'] else [B, A][A['health'] > B['health']]['name'] + ' has won the fight.'
