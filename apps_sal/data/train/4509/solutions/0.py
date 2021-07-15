def is_valid_bar(bar, meter):
    total = 0
    for n in bar:
        n = int(n)
        if n & (n - 1):
            return False
        total += 1.0 / n
    return total == meter

def validate_rhythm(meter, score):
    n, d = meter
    if d & (d - 1):
        return "Invalid rhythm"
    bars = score.split("|")
    meter = float(n) / d
    if all(is_valid_bar(bar, meter) for bar in bars[1:-1]):
        if all(is_valid_bar(bar, meter) for bar in (bars[0], bars[-1])):
                return "Valid rhythm"
        if len(bars) > 1 and is_valid_bar(bars[0] + bars[-1], meter):
                return "Valid rhythm with anacrusis"
    return "Invalid rhythm"
