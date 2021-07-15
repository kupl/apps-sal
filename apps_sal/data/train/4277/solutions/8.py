def difference_in_ages(ages):
    oldest, youngest = max(ages), min(ages)
    diff = oldest - youngest
    return (youngest, oldest, diff)
