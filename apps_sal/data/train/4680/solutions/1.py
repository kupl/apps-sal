def make_change(amount):
    H = 50
    Q = 25
    D = 10
    N = 5
    P = 1
    change = {}
    while amount > 0:
        if (amount - H) >= 0:
            change["H"] = 1
            amount -= H
            while amount >= H:
                change["H"] += 1
                amount -= H
        elif (amount - Q) >= 0:
            change["Q"] = 1
            amount -= Q
            while amount >= Q:
                change["Q"] += 1
                amount -= Q
        elif (amount - D) >= 0:
            change["D"] = 1
            amount -= D
            while amount >= D:
                change["D"] += 1
                amount -= D
        elif (amount - N) >= 0:
            change["N"] = 1
            amount -= N
            while amount >= N:
                change["N"] += 1
                amount -= N
        elif (amount - P) >= 0:
            change["P"] = 1
            amount -= P
            while amount >= P:
                change["P"] += 1
                amount -= P
        else:
            return change
    return change
