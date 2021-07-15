def nb_year(p0, percent, aug, p):
    # your code
    sum = p0
    percent_value = percent / 100
    years = 0
    while (sum < p):
        years +=1
        sum += sum*percent_value + aug
    return years
