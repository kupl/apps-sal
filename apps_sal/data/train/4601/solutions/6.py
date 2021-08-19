def mormons(followers, reach, target):
    mission = 0
    while followers < target:
        followers *= reach + 1
        mission += 1
    return mission
