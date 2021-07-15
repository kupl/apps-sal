def solve(s):
    breakdown = [0]
    for i in s:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            breakdown[-1] = breakdown[-1]*10 + int(i)
        elif breakdown[-1] != 0:
            breakdown.append(0)
    breakdown.sort()
    return(breakdown[-1])
