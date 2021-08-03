def alphabet_war(fight):
    clash = sum('sbpw'.find(e) - 'zdqm'.find(e) for e in fight)

    if clash > 0:
        return 'Left side wins!'
    elif clash < 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
