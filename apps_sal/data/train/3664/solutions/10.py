def cat_mouse(x):
    '''
    takes as input a string (x) featuring a cat 'C'
    and a mouse 'm'. Returns the string "Escaped!" if
    there are more than three characters between 'C' and
    'm', or "Caught!" if three or fewer.
    '''
    if abs(list(x).index('C') - list(x).index('m')) > 4: # tests the absolute value of the differences between the characters' indices
        return "Escaped!"
    else:
        return "Caught!"
