def leaderboard_sort(leaderboard, changes):
    adjustments = leaderboard
    for change in changes:
        adjustment_num = int(change.split(' ')[1])
        name = change.split(' ')[0]
        new_place = adjustments.index(name) - adjustment_num
        adjustments.pop(adjustments.index(name))
        adjustments.insert(new_place, name)
    return adjustments
