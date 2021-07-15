def alphabet_war(fight):
    import re  
    countleft = len(re.findall('w', fight))*4 + len(re.findall('p', fight))*3 + len(
    re.findall('b', fight))*2 + len(re.findall('s', fight))*1
    countright = len(re.findall('m', fight))*4 + len(re.findall('q', fight))*3 + len(
    re.findall('d', fight))*2 + len(re.findall('z', fight))*1
    if countleft == countright:
        return "Let's fight again!"
    elif countright > countleft:
        return "Right side wins!"
    elif countleft > countright:
        return "Left side wins!"
