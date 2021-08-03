def quidditch_scoreboard(teams, actions):
    team_1, team_2 = teams.split(' vs ')[0], teams.split(' vs ')[1]
    fouls = ['Blatching foul', 'Blurting foul', 'Bumphing foul', 'Haverstacking foul', 'Quaffle-pocking foul', 'Stooging foul']
    scores = {'Quaffle goal': 10, 'Caught Snitch': 150}
    scores_1, scores_2 = 0, 0
    for i in actions.split(','):
        if i.split(": ")[0].strip() == team_1:
            if i.split(": ")[1].strip() in scores:
                if i.split(": ")[1].strip() == 'Caught Snitch':
                    scores_1 += scores[i.split(": ")[1].strip()]
                    break
                else:
                    scores_1 += scores[i.split(": ")[1].strip()]
            if i.split(": ")[1].strip() in fouls:
                scores_1 -= 30
        else:
            if i.split(": ")[0].strip() == team_2:
                if i.split(": ")[1].strip() in scores:
                    if i.split(": ")[1].strip() == 'Caught Snitch':
                        scores_2 += scores[i.split(": ")[1].strip()]
                        break
                    else:
                        scores_2 += scores[i.split(": ")[1].strip()]
                if i.split(": ")[1].strip() in fouls:
                    scores_2 -= 30
    return "{}: {}, {}: {}".format(team_1, scores_1, team_2, scores_2)
