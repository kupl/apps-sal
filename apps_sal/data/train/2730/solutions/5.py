def tickets(people, cost=25, bills=[100, 50, 25]):
    count = dict.fromkeys(bills, 0)
    for change in people:
        count[change] += 1
        change -= cost
        for bill in bills:
            if change >= bill:
                c = min(change // bill, count[bill])
                count[bill] -= c
                change -= c * bill
        if change: return "NO"
    return "YES"

