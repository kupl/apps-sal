def greatest_distance(data):
    i = 0
    d = 0
    while (i < len(data)):
        j = i + 1
        while (j < len(data)):
            if (data[j] == data[i]):
                if (j - i > d):
                    d = j - i
            j += 1
        i += 1
    return d
