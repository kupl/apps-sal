def alan(arr):
    stops = ['Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway']
    counter = 0

    for i in stops:
        if i in arr:
            counter += 1

    if counter == len(stops):
        return "Smell my cheese you mother!"
    return "No, seriously, run. You will miss it."
