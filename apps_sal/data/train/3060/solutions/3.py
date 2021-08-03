def get_required(p, e):
    s1, s2 = sum(p), sum(e)
    if s1 >= s2 + 6:
        return "Auto-win"
    elif s2 >= s1 + 6:
        return "Auto-lose"
    elif s1 == s2:
        return "Random"
    elif s1 == s2 - 5:
        return "Pray for a tie!"
    elif s2 > s1:
        return f"(1..{5-(s2-s1)})"
    else:
        return f"({7-(s1-s2)}..6)"
