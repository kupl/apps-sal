import re

def uncollapse(digits):
    return ' '.join(re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine)',digits))
