def sort_by_height(a):
    people = sorted([j for j in a if j != -1])
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = people.pop(0)
    return a
