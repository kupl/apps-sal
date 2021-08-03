import re

WATER_PATTERN = re.compile(r"water|wet|wash", re.I)
SLIME_PATTERN = re.compile(r"\bI don't know\b|slime", re.I)


def bucket_of(said):
    water = WATER_PATTERN.search(said)
    slime = SLIME_PATTERN.search(said)

    if water:
        return 'sludge' if slime else 'water'

    return 'slime' if slime else 'air'
