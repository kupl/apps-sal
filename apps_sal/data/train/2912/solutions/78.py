def find_multiples(integer, limit):
    li = []
    for x in range(1,limit+1):
        if x % integer == 0:
            li.append(x)
    return li
