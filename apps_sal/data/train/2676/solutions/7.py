def find_needed_guards(k):
    total = 0
    for i in range(1, len(k)):
        if k[i] == False:
            if k[i - 1] == False:
                total += 1
                k[i] = True
    return total
