def quidditch_scoreboard(t, s, x=0, y=0):
    a, b = t.split(' vs ')
    for X in s.split(','):
        k, v = X.strip().split(':')
        if k == a:
            x += 10if' Quaffle goal' == v else 150if' Caught Snitch' == v else -30
        if k == b:
            y += 10if' Quaffle goal' == v else 150if' Caught Snitch' == v else -30
        if ' Caught Snitch' == v:
            break
    return '%s: %d, %s: %d' % (a, x, b, y)
