def is_balanced(verify, pairs):
    opened,closed,records,same = [],[],[],[]
    for i in range(0, len(pairs), 2):
        opened.append(pairs[i])
        closed.append(pairs[i + 1])
    for i in verify:
        if i in opened and i in closed : same.append(not verify.count(i) & 1)
        elif i in opened : records.append(i)
        elif i in closed:
            if not records:return 0
            if records[-1] == opened[closed.index(i)] : records.pop()
    return not records and all(same)
