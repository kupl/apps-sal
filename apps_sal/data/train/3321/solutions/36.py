def evil(n):
    bin_rep = str(bin(n))
    state = "Evil" if bin_rep.count("1") % 2 == 0 else "Odious"
    return f"It's {state}!"
