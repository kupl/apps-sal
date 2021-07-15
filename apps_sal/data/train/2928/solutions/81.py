def alphabet_war(fight):
    winner = sum(' zdqm'.index(x) for x in fight if x in 'zdqm') - sum(' sbpw'.index(x) for x in fight if x in 'sbpw')
    return "Left side wins!" if winner < 0 else "Right side wins!" if winner > 0 else "Let's fight again!"
