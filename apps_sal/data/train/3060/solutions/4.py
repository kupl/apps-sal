def get_required(player,enemy):
    p, e = sum(player), sum(enemy)
    if p == e:
        return "Random"
    elif p-e>=6:
        return "Auto-win"
    elif e-p>=6: 
        return "Auto-lose"
    elif p > e:
        return f"({e-p+7}..6)"
    elif e - p < 5 :
        return f"(1..{p+5-e})" 
    return "Pray for a tie!"
