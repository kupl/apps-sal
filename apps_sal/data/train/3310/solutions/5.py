def score_pole_vault(vaulter_list):
    summary = []
    for i in vaulter_list:
        total_X = 0
        highest_cleared = -1
        X_at_highest = 0
        for j in range(len(i['results'])):
            if 'O' in i['results'][j]:
                highest_cleared = j
                X_at_highest = i['results'][j].count('X')
            total_X += i['results'][j].count('X')
        summary.append((-highest_cleared, X_at_highest, total_X, i['name']))
    final_standing = sorted(summary)
    result = {}
    winners_stat = final_standing[0][:3]
    winners = []
    for i in final_standing:
        if i[:3] == winners_stat[:3]:
            winners.append(i[3])
    result['1st'] = ', '.join(winners) + ' (jump-off)' * (len(winners) > 1)
    if len(winners) > 2:
        return result
    if len(winners) == 1:
        second_stat = final_standing[1][:3]
        seconds = []
        for i in final_standing:
            if i[:3] == second_stat[:3]:
                seconds.append(i[3])
        result['2nd'] = ', '.join(seconds) + ' (tie)' * (len(seconds) > 1)
        if len(seconds) > 1:
            return result
    thirds = []
    third_stat = final_standing[2][:3]
    for i in final_standing:
        if i[:3] == third_stat[:3]:
            thirds.append(i[3])
    result['3rd'] = ', '.join(thirds) + ' (tie)' * (len(thirds) > 1)
    return result
