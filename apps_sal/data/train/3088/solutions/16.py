from typing import Union

def nba_extrap(ppg: Union[int, float], mpg: int) -> Union[int, float]:
    """ Get a straight extrapolation of points per game per 48 minutes game. """
    return 0 if any([not ppg, not mpg]) else round(48 / mpg * ppg, 1)
