def sum_two_smallest_numbers(L):
    x=min(L) #take the lowest number and stock it
    L.remove(x) #remove it from the list
    y=min(L) #take the new lowest number and stock it
    return x+y

