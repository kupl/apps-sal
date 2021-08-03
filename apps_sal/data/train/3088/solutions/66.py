NBA_GAME_TIME = 48


def nba_extrap(points_per_game: float, minutes_per_game: float) -> float:
    if minutes_per_game < 0.001:
        return 0.0
    else:
        return round(points_per_game / minutes_per_game * NBA_GAME_TIME, 1)
