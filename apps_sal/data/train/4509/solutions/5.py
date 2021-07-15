def validate_rhythm(meter, score):
    from fractions import Fraction
    if meter[1] not in [1,2,4,8]:
        return 'Invalid rhythm'
    
    time_signature = Fraction(*meter)
    bars = [sum(Fraction(1, int(c)) for c in bar) for bar in score.split('|')]

    if all(bar == time_signature for bar in bars):
        return 'Valid rhythm'
    
    if all(bar == time_signature for bar in bars[1:-1]) and bars[0] + bars[-1] == time_signature:
        return 'Valid rhythm with anacrusis'
        
    return 'Invalid rhythm'
