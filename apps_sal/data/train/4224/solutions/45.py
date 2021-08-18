

def dont_give_me_five(start, end):
    """ function that returns the count of numbers between start and end (inclusive), 
        except for those containing 5 """
    count = 0
    for i in range(start, end + 1):
        if '5' in str(i):
            pass
        else:
            count += 1
    return count
