from operator import itemgetter


def fight(r1, r2, tactics):

    i, bots = 0, sorted((r2, r1), key=itemgetter('speed'))
    for r in bots:
        r['tactics'] = r['tactics'][::-1]

    while 1:
        i ^= 1
        if bots[i]['tactics']:
            bots[i ^ 1]['health'] -= tactics[bots[i]['tactics'].pop()]

        if bots[i ^ 1]['health'] <= 0 or all(not r['tactics'] for r in bots):
            break

    a, b = bots
    cmp = (a['health'] < b['health']) - (a['health'] > b['health'])

    return "The fight was a draw." if not cmp else f"{bots[max(cmp,0)]['name']} has won the fight."
