import re

def alphabet_war(fight):
    pattern = re.compile(r"(\w)?\*+(\w)?")
    powers = pattern.sub("", fight)
    scores = "mqdz*sbpw" 
    score = sum(i * powers.count(p) for i, p in enumerate(scores, -4))
    return ["Let's fight again!", "Left side wins!", "Right side wins!"][(score>0)-(score<0)]
