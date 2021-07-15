next_higher = lambda x : x + (x & -x) | (x ^ x + (x & -x)) // (x & -x) >> 2 

