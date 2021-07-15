import re

def err_bob(s):
    return re.sub(
        r'[bcdfghjklmnpqrstvwxyz]\b',
        lambda m: m.group() + ('err' if m.group().islower() else 'ERR'),
        s,
        flags=re.IGNORECASE
    )
