def bumps(road):
    road_list = list(road)
    bump_number = 0
    for segment in road_list:
        if segment == 'n':
            bump_number += 1
    if bump_number <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"
