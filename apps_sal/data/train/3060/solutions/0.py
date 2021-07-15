def get_required(player,enemy):
    p_sum = sum(player)
    e_sum = sum(enemy)
    
    diff = p_sum - e_sum
    
    if diff == 0:
        return 'Random'
    
    if diff > 5:
        return 'Auto-win'
    
    if diff < -5:
        return 'Auto-lose'
    
    if diff == -5:
        return 'Pray for a tie!'
    
    s = ''
    
    if diff < 0:
        s = '(1..{0})'.format(6-abs(diff)-1)
    else:
        s = '({0}..6)'.format(6-diff+1)
    
    return s
