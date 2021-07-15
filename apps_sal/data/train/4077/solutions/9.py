def premier_league_standings(teams):
    t = sorted(teams.items(), key=lambda i:str(i[0]) if i[0]==1 else i[1])
    return {i+1:t[i][1] for i in range(len(t))}
