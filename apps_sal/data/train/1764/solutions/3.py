def solve(emulator):
    num_drops = emulator.drops
    num_eggs = emulator.eggs
    floor = 0

    def height(eggs, drops):
        max_floor = 0
        if eggs <= 0:
            return 0
        elif eggs == 1:
            return drops
        else:
            for x in range(1, drops + 1):
                max_floor += height(eggs - 1, drops - x) + 1
            return max_floor

    while num_drops and num_eggs:
        temp = height(num_eggs - 1, num_drops - 1) + 1
        if not emulator.drop(floor + temp):
            floor += temp
            num_drops -= 1
        else:
            num_eggs -= 1
            num_drops -= 1

    return floor + 1
