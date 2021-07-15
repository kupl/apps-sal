from typing import Dict

def char_freq(message: str) -> Dict[int, str]:
    """ Get the frequency of each and every character! """
    return dict([(_, message.count(_)) for _ in sorted(set(message))])
