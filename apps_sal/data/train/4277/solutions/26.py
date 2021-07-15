def difference_in_ages(ages):
    ages = sorted(ages)
    return (ages[0], ages[len(ages)-1], abs(ages[0] - ages[len(ages)-1 ]))
