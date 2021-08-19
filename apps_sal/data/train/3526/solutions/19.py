def any_arrows(q):
    return 1 - all((a.get('damaged') for a in q))
