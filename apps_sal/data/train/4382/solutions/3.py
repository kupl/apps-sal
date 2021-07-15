import re

def uncollapse(digits):
    return re.sub(r'(zero|one|two|three|four|five|six|seven|eight|nine)',r'\1 ',digits).strip()
