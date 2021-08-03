from typing import List


def points(games: List[str]) -> int:
    """ Counts the points of the team in the championship. """
    points = 0
    results = [(int(goals[0]), int(goals[1])) for goals in [score.split(":") for score in games]]
    for (scored_goals, lost_goals) in results:
        if scored_goals > lost_goals:
            points += 3
        elif scored_goals == lost_goals:
            points += 1
    return points
