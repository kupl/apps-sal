def scratch(lottery):
    ans = 0
    for ticket in lottery:
        t = ticket.split()
        if t.count(t[0]) == 3:
            ans += int(t[3])
    return ans
