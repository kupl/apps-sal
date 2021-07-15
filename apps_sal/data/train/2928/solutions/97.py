left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

def alphabet_war(fight):
    #your code here
    counter_left = 0
    counter_right = 0

    for letter in fight:
        if letter in left:
            counter_left += left[letter]
        elif letter in right:
            counter_right += right[letter]

    if counter_left > counter_right:
        return 'Left side wins!' 
    elif counter_left < counter_right:
        return 'Right side wins!' 
    else:
        return "Let's fight again!"
