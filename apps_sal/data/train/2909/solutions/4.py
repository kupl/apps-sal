is_tune=lambda Q:bool(Q)and any(all((B-V)%12in(0,2,4,5,7,9,11)for B in Q)for V in range(12))
