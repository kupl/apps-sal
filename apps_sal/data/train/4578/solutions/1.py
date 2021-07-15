def quidditch_scoreboard(teams, actions):

    def formatter(team, pts): return ', '.join(f'{t}: {p}' for p,t in zip(pts,teams))

    pts, teams = [0,0], teams.split(' vs ')
    for act in actions.split(', '):
        for i,t in enumerate(teams):
            p = act.startswith(t) * (10*act.endswith('goal') + 150 * act.endswith('Snitch') - 30*act.endswith('foul'))
            pts[i] += p
            if p==150: return formatter(teams, pts)
    return formatter(teams,pts)
