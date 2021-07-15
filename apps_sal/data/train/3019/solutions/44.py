def str_count(strng, letter):
    arr = []
    for j in letter:
        for i in strng:
            if j == i:
                arr.append(j)
    return len(arr)

