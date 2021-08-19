import re
pattern = re.compile('zero|one|two|three|four|five|six|seven|eight|nine')


def uncollapse(digits):
    return ' '.join(pattern.findall(digits))
