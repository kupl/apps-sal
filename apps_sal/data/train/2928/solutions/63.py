def alphabet_war(fight):
    left_side = []
    right_side = []
    for elem in fight:
        if elem == "w":
            left_side.append(4)
        elif elem == "p":
            left_side.append(3)
        elif elem == "b":
            left_side.append(2)
        elif elem == "s":
            left_side.append(1)
        elif elem == "m":
            right_side.append(4)
        elif elem == "q":
            right_side.append(3)
        elif elem == "d":
            right_side.append(2)
        elif elem == "z":
            right_side.append(1)
    
    print(right_side)
    if sum(left_side) > sum(right_side):
        return "Left side wins!"
    elif sum(left_side) < sum(right_side):
        return "Right side wins!"
    else:
        return "Let's fight again!"
