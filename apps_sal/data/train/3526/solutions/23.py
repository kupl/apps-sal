from typing import List, Dict, Union

def any_arrows(arrows: List[Dict[str, Union[int, bool]]]) -> int:
    """ Get status that you have some good ones left, in order to prepare for battle. """
    return bool(next(filter(lambda _arr: not _arr.get("damaged", False), arrows), False))
