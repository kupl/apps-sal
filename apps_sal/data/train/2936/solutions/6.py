def num_of_open_lockers(n):
    print("lockers:", n)

    i = 0
    count = 1
    open = 0
    even = True
    while i < n:
        if even:
            i += 1
            open += 1
            even = False
        else:
            even = True
            i += count * 2
            count += 1

    # print "open:", open
    return open
