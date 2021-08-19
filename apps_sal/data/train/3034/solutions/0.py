def bowling_score(rolls):
    """Compute the total score for a player's game of bowling."""

    def is_spare(rolls):
        return 10 == sum(rolls[:2])

    def is_strike(rolls):
        return 10 == rolls[0]

    def calc_score(rolls, frame):
        return sum(rolls) if frame == 10 else sum(rolls[:3]) + calc_score(rolls[1:], frame + 1) if is_strike(rolls) else sum(rolls[:3]) + calc_score(rolls[2:], frame + 1) if is_spare(rolls) else sum(rolls[:2]) + calc_score(rolls[2:], frame + 1)
    return calc_score(rolls, 1)
