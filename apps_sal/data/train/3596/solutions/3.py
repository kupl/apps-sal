def membership(amount, platinum, gold, silver, bronze):
    l = locals()
    a = l.pop('amount')
    try:
        return max(((v, e) for (e, v) in l.items() if a >= v))[1].capitalize()
    except:
        return 'Not a member'
