def ulam_sequence(u, v, n):
    lst, seq, ex, q = [], 1, 1, 1 << v | 1 << u  # Put u and v into queue
    for _ in range(n):                           # Repeat n times
        w = q & -q                               # Take the smallest candidate
        l = w.bit_length() - 1                   # and its value
        s = seq << l                             # Generate its sums with all previous values
        seq |= w                                 # Append it afterwards to the sequence
        lst.append(l)                            # and to the list
        ex |= s & q                              # Update excluded values if any is already in queue
        q |= s                                   # Put previous sums into queue
        q &= ~ex                                 # Remove excluded values from queue
    return lst                                   # Return sequence list
