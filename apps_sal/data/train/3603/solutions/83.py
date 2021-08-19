# input - two integers represting flower petals
#output - boolean
# edge cases - string given, no input given, decimals/flaots given
# assumptions - solve by comparing first integer to second integer, same number is False
# data types - integers
# end goal - function returns True if one of the flowers has an odd number of petals
# and the other has an even number, else False

# sample data (1,4) = True
# (6,8) = False
# ("4",7) = False
# (3.4,8) = True

# function takes flower1 and flower2
def lovefunc(flower1, flower2):
    # check if flower1 and flower2 are both even
    if flower1 % 2 == 0 and flower2 % 2 == 0:
        # if they are even, return false
        return False
# check if both flowers are odd
    elif flower1 % 2 != 0 and flower2 % 2 != 0:
        # if they are odd, return false
        return False
# return True if you have one odd and one even
    else:
        return True
