def solve(emulator):
    print("Drops")
    print((emulator.drops))
    num_drops = emulator.drops
    print("Eggs")
    print((emulator.eggs))
    num_eggs = emulator.eggs
    currFloor = 0
    broke = False
    maxFloor = -1
    minFloor = 0
    print((next_jump(num_eggs + 1, num_drops + 1)))

    while emulator.drops > 0 and emulator.eggs > 0:
        if emulator.eggs == 1:
            currFloor += 1
            print(currFloor)
            broke = emulator.drop(currFloor)
            if broke:
                return currFloor
            else:
                minFloor = currFloor
        elif emulator.eggs == 2:
            currFloor += emulator.drops
            print(currFloor)
            broke = emulator.drop(currFloor)
            if broke:
                maxFloor = currFloor
                currFloor = minFloor
            else:
                minFloor = currFloor
        else:
            num_drops = emulator.drops
            num_eggs = emulator.eggs
            currFloor += next_jump(num_eggs, num_drops)
            print(("up  by: " + str(next_jump(num_eggs, num_drops)) + " eggs: " + str(num_eggs) + " drops: " + str(num_drops)))
            print(currFloor)
            broke = emulator.drop(currFloor)
            if broke:
                maxFloor = currFloor
                currFloor = minFloor
            else:
                minFloor = currFloor
    return currFloor + 1


def find_sum_to_current(dropCount):
    number = 0
    for i in range(1, dropCount + 1):
        number += i
    return number


def next_jump(num_egg, num_drop):
    if num_egg == 1 or num_drop == 1:
        return 1
    else:
        sum = 0
        for i in range(0, num_drop):
            sum += next_jump(num_egg - 1, i)
        if(num_egg > 2):
            sum += 1
        return sum
