
def digitize(n):
    return list(reversed([int(x) for x in str(n)])) #reversed(sequence),here sequence
                                                    #is a list comprehension returns an 
                                                    #object which is accessed by using a list
                                                    #which is in this case.

