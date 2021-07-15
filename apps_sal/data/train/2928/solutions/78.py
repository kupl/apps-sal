def alphabet_war(fight):
    right = {
        'm' : 4,
        'q' : 3,
        'd' : 2,
        'z' : 1,
    }
    
    left = {
         'w' : 4,
         'p' : 3,
         'b' : 2,
         's' : 1,
    }
    
    left_count = 0
    right_count = 0
    
    right, left = right.items(),left.items()

    for right_letter, left_letter in zip(right, left):
        for letter in fight:
            if letter == right_letter[0]:
                right_count += right_letter[1] 

            if letter == left_letter[0]:
                left_count += left_letter[1]    

    if left_count > right_count: return "Left side wins!"
    elif right_count > left_count: return "Right side wins!"
    elif right_count == left_count: return "Let's fight again!"
