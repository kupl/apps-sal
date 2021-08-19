import re


def uncollapse(digits):
    return re.sub('(zero|one|two|three|four|five|six|seven|eight|nine)', '\\1 ', digits).strip()
