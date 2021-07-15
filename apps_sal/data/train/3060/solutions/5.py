def get_required(player, enemy):
    p = sum(player)
    e = sum(enemy)
    if p==e: 
        return 'Random'
    elif p+6<=e: 
        return "Auto-lose"
    elif p>=e+6: 
        return "Auto-win"
    elif p+6==e+1: 
        return "Pray for a tie!"
    elif p>e: 
        return f'({6+e-p+1}..6)'
    else: 
        return f'(1..{6+p-e-1})'
