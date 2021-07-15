def alphabet_war(fight):
    left = {'w':4, 'p':3, 'b':2, 's':1}
    right = {'m':4, 'q':3, 'd':2, 'z':1}
    left_side = 0
    right_side = 0
    for elem in fight:
        if elem in left.keys():
            left_side = left_side + left[elem]
        elif elem in right.keys():
            right_side = right_side + right[elem]
    return 'Left side wins!' if left_side >right_side  else ('Right side wins!'  if left_side < right_side  else "Let's fight again!")
