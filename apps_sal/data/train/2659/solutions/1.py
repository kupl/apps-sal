def last_chair(n):
    # Propn:
    #   Given there are n seats, n >= 2. The (n-1)th seat is always the
    #   last to be taken (taken in iteration n).
    # Proof:
    #   Suppose that, for some n >= 2, the (n-1)th seat is taken on
    #   iteration i > 2. The nth seat is already taken, since the 2nd
    #   iteration will always claim it. Therefore i must sit beside
    #   at least one person (the occupant of seat n).
    #   Additionally, the (n-2)th seat must also already be taken.
    #   If it were not taken, (n-2) would have a free seat at (n-1)
    #   and would be closer to the exit, and so would rank higher
    #   than (n-1) in the choice algorithm.
    #   Therefore (n-1) will only be chosen when (n-2) and (n) are
    #   both taken.
    #   Also, all other seats must also be taken, since
    #   otherwise i would taken them, having at most as many people
    #   around as seat (n-1) and being closer to the exit.
    #   Therefore (n-1) is the last seat to be taken.
    return n - 1
