# create a count variable and set to 0
# iterate through start and end + 1:
#   if '5' is in str(num): pass 
#   else: count += 1
# return the count


def dont_give_me_five(start,end):
    """ function that returns the count of numbers between start and end (inclusive), 
        except for those containing 5 """
    count = 0  # number of numbers between start and end+1, excluding 5's
    for i in range(start, end+1):
        if '5' in str(i):    # does not count numbers with '5'
            pass
        else:
            count += 1
    return count   # returns int 
