def monkey_count(n):
    list = []
    for i in range(n+1):
        i += 1
        list.append(i)
        if i == (n):
            break
        else:
            continue
    return list
