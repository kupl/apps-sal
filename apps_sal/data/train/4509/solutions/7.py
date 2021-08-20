def validate_rhythm(meter, score):
    (a, b) = meter
    if not set(score) <= set('1248|') or b not in (1, 2, 4, 8):
        return 'Invalid rhythm'
    bars = [sum((1 / int(x) for x in bar)) for bar in score.split('|')]
    m = a / b
    if all((x == m for x in bars)):
        return 'Valid rhythm'
    if len(bars) >= 2 and all((x == m for x in bars[1:-1] + [bars[0] + bars[-1]])):
        return 'Valid rhythm with anacrusis'
    return 'Invalid rhythm'
