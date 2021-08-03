def scratch(lottery):
    result = 0
    for ticket in lottery:
        words = ticket.split()
        if words[0] == words[1] == words[2]:
            result += int(words[3])
    return result
