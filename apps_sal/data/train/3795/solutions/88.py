def combat(health, damage):
    case = health - damage
    if case < 0:
        case = 0
    return case

