import re

def uncollapse(digits):
    return ' '.join(re.findall('one|two|three|four|five|six|seven|eight|nine|zero', digits))
