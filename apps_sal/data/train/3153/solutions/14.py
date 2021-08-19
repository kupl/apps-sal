from typing import Union


def playerRankUp(pts: int) -> Union[int, str]:
    """
    Check if the player has achieved at least 100 points in his class.
    If so, he enters the qualifying stage with congratulations message.
    """
    return {pts >= 100: 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'}.get(True, False)
