def game(a, b):
    print((a, b))
    if a == 0 or b == 0:
        return "Non-drinkers can't play"
    (sa, sb) = (1, 2)
    while True:
        if a - sa < 0:
            return 'Joe'
        a -= sa
        sa += 2
        if b - sb < 0:
            return 'Mike'
        b -= sb
        sb += 2
