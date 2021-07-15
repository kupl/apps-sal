def better_than_average(array, points):
    average = (sum(array) / (len(array) - 1))
    if points >= average:
        return True
    else:
        return False

