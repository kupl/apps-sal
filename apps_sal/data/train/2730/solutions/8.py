def tickets(people):
    change = []
    try:
        for cash in people:
            if cash == 25:
                change.append(25)
            if cash == 50:
                change.remove(25)
                change.append(50)
            if cash == 100 and (50 in change):
                change.remove(50)
                change.remove(25)
            elif cash == 100:
                change.remove(25)
                change.remove(25)
                change.remove(25)
    except:
        return "NO"
    else:
        return "YES"
