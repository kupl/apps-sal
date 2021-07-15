from typing import List, Dict, Union


def any_arrows(arrows: List[Dict[str, Union[str, bool]]]) -> bool:
    return any(not a.get('damaged', False) for a in arrows)

