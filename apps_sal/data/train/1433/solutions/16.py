t = int(input())
for i in range(t):
    a = input()
    b = input()
    sa, sb, fa, fb, ac1, ac2, bc1, bc2 = 0, 0, 0, 0, 0, 0, 0, 0
    for x in a:
        if x < '4':
            ac1 += 1
        elif x == '4':
            fa += 1
        elif x < '7':
            ac2 += 1
        elif x == '7':
            sa += 1
    for x in b:
        if x < '4':
            bc1 += 1
        elif x == '4':
            fb += 1
        elif x < '7':
            bc2 += 1
        elif x == '7':
            sb += 1

    final7, final4 = 0, 0

    if sa:
        x = sa if bc2 > sa else bc2
        final7 += x
        sa -= x
        bc2 -= x
        x = sa if bc1 > sa else bc1
        final7 += x
        sa -= x
        bc1 -= x
        if sa:
            x = sa if fb > sa else fb
            final7 += x
            sa -= x
            fb -= x
    if sb:
        x = sb if ac2 > sb else ac2
        final7 += x
        sb -= x
        ac2 -= x
        x = sb if ac1 > sb else ac1
        final7 += x
        sb -= x
        ac1 -= x
        if sb:
            x = sb if fa > sb else fa
            final7 += x
            sb -= x
            fa -= x
    if fa:
        x = fa if bc1 > fa else bc1
        final4 += x
        fa -= x
        bc1 -= x
    if fb:
        x = fb if ac1 > fb else ac1
        final4 += x
        fb -= x
        ac1 -= x
    final4 += min(fa, fb)
    final7 += min(sa, sb)
    print('7' * final7 + '4' * final4)
