def validate_rhythm(meter, score):
    if meter[1] not in (1,2,4,8):
        return "Invalid rhythm"
    
    score = score.translate(score.maketrans("1248", "8421"))
    target = meter[0] * 8 // meter[1]
    
    def valid(s):
        return sum(int(c) for c in s) == target
    
    bars = score.split("|")
    if any(not valid(bar) for bar in bars[1:-1]):
        return "Invalid rhythm"
    
    if valid(bars[0]) and valid(bars[-1]):
        return "Valid rhythm"
    
    if valid(bars[0] + bars[-1]):
        return "Valid rhythm with anacrusis"
    else:
        return "Invalid rhythm"
