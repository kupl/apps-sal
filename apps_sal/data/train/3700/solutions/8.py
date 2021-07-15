def kooka_counter(laugh):
    count = 0
    while laugh:
        pat = laugh[:2]
        laugh = laugh.lstrip(pat)
        count += 1
    return count
