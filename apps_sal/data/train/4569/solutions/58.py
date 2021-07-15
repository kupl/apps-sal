def next_item(xs, item):
    find=False
    findValue=None
    for i in xs:
        if find:
            findValue=i
            break
        if i==item:
            find=True
    return findValue
