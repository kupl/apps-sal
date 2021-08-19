def nba_extrap(ppg, mpg):
    return round(48 * ppg / mpg, 1)


"An NBA game runs 48 minutes (Four 12 minute quarters).\nPlayers do not typically play the full game, subbing in and out as necessary. \nYour job is to extrapolate a player's points per game if they played the full 48 minutes.\n\nWrite a function that takes two arguments, ppg (points per game) and mpg (minutes per game)\nand returns a straight extrapolation of ppg per 48 minutes rounded to the nearest tenth. \nReturn 0 if 0."
