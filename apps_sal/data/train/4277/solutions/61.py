def difference_in_ages(ages):
    ages.sort()
    tpp1 = (ages[0], ages[-1], ages[-1] - ages[0])
    return tpp1
