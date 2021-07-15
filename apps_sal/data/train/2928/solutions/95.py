def alphabet_war(fight):
    d = {"w": -4, "p": -3, "b": -2, "s": -1, "m": 4, "q": 3, "d": 2, "z": 1}
    
    score = sum([d.get(char, 0) for char in fight])
    
    if score == 0:
        msg = "Let's fight again!"
    elif score < 0:
        msg = "Left side wins!"
    else:
        msg = "Right side wins!"
            
    return msg

