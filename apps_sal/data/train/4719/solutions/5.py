def sort_array(a):
    # Create two sorted arrays one containing even and on odd numbers. Each array 
    # is sorted opposite of the desired results as we will pop items off the array.
    sorted_odd = sorted([x for x in a if x % 2 == 1], reverse=True)
    sorted_even = sorted([x for x in a if x % 2 == 0])
    
    # Build the final output. Place the sorted even numbers where even numbers were
    # in the original list and sorted odd numbers where odd numbers were in the 
    # original list.
    out = []
    for x in a:
        if x % 2 == 0:
            out.append(sorted_even.pop())
        else:
            out.append(sorted_odd.pop())
            
    return out

