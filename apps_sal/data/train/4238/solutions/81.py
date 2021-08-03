# Okay, why not try an "upwards" recursive solution
# Note: The BASE CASE is the one that supplies the final result back to the calling (test) code
#       so we still only get one value passed back to the calling code.
# Madness or magic? Such is the curse of recursive code!

def squares_needed(grains, steps_taken=0):   # added an extra param. Initial call (from test) defaults to 0
    if grains < 2 ** steps_taken:             # if the # of grains can be met by the 0-index square we're on...
        return steps_taken                     # ...return that square
    else:
        steps_taken += 1                       # ...if not, increase the square we're on by 1...
        return squares_needed(grains, steps_taken)  # ...and try again


# Previous submission was iterative (basic but fairly easy to grasp I think)
# def squares_needed(grains):
#    if grains == 0:
#        return grains

#    total = 0

#    for i in range(0, 65):
#        total += 2**i

#        if  grains <= total:
#            return i + 1
