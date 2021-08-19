def alphabet_war(fight):
    # your code here
    left = 0
    right = 0
    for i in fight:
        if i == "w":
            left += 4
        elif i == "p":
            left += 3
        elif i == "b":
            left += 2
        elif i == "s":
            left += 1
        elif i == "m":
            right += 4
        elif i == "q":
            right += 3
        elif i == "d":
            right += 2
        elif i == "z":
            right += 1
    if right > left:
        return "Right side wins!"
    elif left > right:
        return "Left side wins!"
    else:
        return "Let's fight again!"
