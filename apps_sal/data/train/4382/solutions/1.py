import re


def uncollapse(digits):
    return ' '.join(m.group() for m in re.finditer(r'zero|one|two|three|four|five|six|seven|eight|nine', digits))
