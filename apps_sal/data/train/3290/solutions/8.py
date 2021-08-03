def get_ages(sum, difference):
    age1 = (sum + difference) / 2
    age2 = sum - age1
    if sum < 0 or difference < 0 or age1 < 0 or age2 < 0:
        return None
    if age1 > age2:
        return age1, age2
    else:
        return age2, age1
