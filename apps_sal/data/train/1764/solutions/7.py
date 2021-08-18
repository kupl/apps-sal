flockhash = {}


def solve(emulator):

    num_drops = emulator.drops
    num_eggs = emulator.eggs

    def climbing(eggs, drops):

        if eggs == 1:
            return 1
        everest = flockhash.get((eggs, drops))
        if everest != None:
            return everest
        everest = 1
        for kamikaze in range(1, drops):
            everest += climbing(eggs - 1, drops - kamikaze)
        flockhash[(eggs, drops)] = everest
        return everest

    last_broken_egg = 1
    floor = 1 + climbing(num_eggs, num_drops)
    exfloor = 1

    while num_eggs and num_drops:

        if emulator.drop(floor):
            last_broken_egg = floor
            num_eggs -= 1
            floor = exfloor
        else:
            exfloor = floor

        num_drops -= 1
        floor += climbing(num_eggs, num_drops)
    else:

        return last_broken_egg
