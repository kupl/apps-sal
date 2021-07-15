def difference_in_ages(ages):
    sorta = sorted(ages)
    return (sorta[0], sorta[-1], sorta[-1] - sorta[0])
