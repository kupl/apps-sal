def mormons(starting_number, reach, target):
    missions = 0
    while starting_number < target:
        starting_number += starting_number * reach
        missions += 1
    return missions
