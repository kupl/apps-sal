def denumerate(e):
    if type(e) != list or any(type(i) != tuple for i in e) or sorted([i[0] for i in e]) != list(range(0, len(e))):
        return False
    li = "".join([i[1] for i in sorted(e) if len(i[1]) == 1 and i[1].isalnum() and len(i) == 2])
    return li if len(li) == len(e) else False
