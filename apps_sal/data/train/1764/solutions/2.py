def max_floor(eggs, drops):
    return sum(max_floor(eggs-1, d) + 1 for d in range(drops)) if eggs else 0

def solve(emulator):
    floor = 1
    while emulator.eggs and emulator.drops:
        while emulator.drops:
            test = floor + max_floor(emulator.eggs-1, emulator.drops-1) + 1
            if emulator.drop(test): break
            floor = test
    return floor+1

