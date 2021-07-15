import re

def uncollapse(digits):
    pattern = 'zero|one|two|three|four|five|six|seven|eight|nine'
    return ' '.join(re.findall(pattern, digits))
