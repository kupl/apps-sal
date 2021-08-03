def solve(emulator):
    print("Drops")
    print((emulator.drops))
    num_drops = emulator.drops
    print("Eggs")
    print((emulator.eggs))
    num_eggs = emulator.eggs
    currFloor = 0
    broke = False
    maxFloor = -1  # initial state
    minFloor = 0
    # print(find_sum_to_current(num_drops))
    print((next_jump(num_eggs + 1, num_drops + 1)))

    # make max floor based on eggs to the power of dropc count ( -1, -1)
    # then do lion in desert based on the new range - calc is a little different, must think of cases where eggs always break
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
                #currFloor = maxFloor - emulator.drops * (emulator.eggs)
                currFloor = minFloor  # + emulator.eggs
            else:
                minFloor = currFloor
        else:
            num_drops = emulator.drops
            num_eggs = emulator.eggs
            # currFloor += 1 + maxFindRange((num_eggs - 1,num_drops - 1)#maybe +1
            currFloor += next_jump(num_eggs, num_drops)
            print(("up  by: " + str(next_jump(num_eggs, num_drops)) + " eggs: " + str(num_eggs) + " drops: " + str(num_drops)))
            print(currFloor)
            broke = emulator.drop(currFloor)
            if broke:
                maxFloor = currFloor
                currFloor = minFloor  # + emulator.eggs
            else:
                minFloor = currFloor
    return currFloor + 1


# def maxFindRange(eggCount, dropCount):
#    if eggCount >= dropCount:
#        return dropCount#find_sum_to_current(dropCount)#dropCount + 1
#    elif eggCount == 1:
#        return dropCount
#    elif eggCount == 2:
#        return find_sum_to_current(dropCount)
#    else:
#        number = 0#maybe 0 or 1
#        for i in range (1, dropCount + 1):
#            #number += (eggCount - 2) * (find_sum_to_current(dropCount - i - 1) - 1)
#            number += #1 + (eggCount - 2) * (find_sum_to_current(dropCount - i - 1))
#            #solve for negative numbers
#        return number + maxFindRange(eggCount - 1, dropCount - 1)
#    #returns the highest amount that can be tested

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

    # continue here
