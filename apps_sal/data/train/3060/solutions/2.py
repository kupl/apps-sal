def get_required(player, enemy):
    p = player[0] + player[1]
    e = enemy[0] + enemy[1]

    if p == e:
        return "Random"
    elif p > e:
        if (p - 6) >= e:
            return "Auto-win"
        else:
            return "(%d..6)" % ((e + 7) - p)
    elif p < e:
        if p <= (e - 6):
            return "Auto-lose"
        elif (e - p) == 5:
            return "Pray for a tie!"
        else:
            return "(1..%d)" % ((p + 5) - e)
