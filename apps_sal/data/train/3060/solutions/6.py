def get_required(player, enemy):
    difference = player[0] + player[1] - enemy[0] - enemy[1]
    if difference >= 6:
        return 'Auto-win'
    elif difference <= -6:
        return 'Auto-lose'
    elif difference == -5:
        return 'Pray for a tie!'
    elif difference == 0:
        return 'Random'
    elif difference > 0:
        return '(' + str(6 - difference + 1) + '..' + '6)'
    else:
        return '(1' + '..' + str(6 - abs(difference - 1)) + ')'
