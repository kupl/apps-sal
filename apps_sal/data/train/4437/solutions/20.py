from typing import Any

def cookie(x: Any) -> str:
    """ Get an information who ate the last cookie. """
    cookie_eaters = {
        type(x) is str: "Zach",
        type(x) in (float, int): "Monica"
    }
    return f"Who ate the last cookie? It was {cookie_eaters.get(True, 'the dog')}!"
