import re


def uncollapse(s):
    return ' '.join(re.findall('zero|nine|one|eight|two|seven|three|six|four|two|five', s))
