def difference_in_ages(ages):
    # your code here
    oldest = ages[0]
    youngest = ages[0]

    for e in ages:
        if e > oldest:
            oldest = e
        elif e < youngest:
            youngest = e
    arr = ((youngest), (oldest), (oldest - youngest))
    return arr
