import re

def quidditch_scoreboard(teams, actions):
    points = {"goal": 10, "foul": -30, "Caught": 150}
    teams = teams.split(" vs ")
    scores = [0, 0]
    actions = re.findall(r"(\w[\w ]+): .*?(goal|foul|Caught)", actions.partition(" Snitch")[0])
    for team, action in actions:
        scores[teams.index(team)] += points[action]
    return "{0[0]}: {1[0]}, {0[1]}: {1[1]}".format(teams, scores)
