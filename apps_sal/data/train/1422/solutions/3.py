inputs = int(input())
while inputs > 0:
    length = int(input())
    building = input()
    buildings = []
    if length != 0:
        for i in range(0, length):
            buildings.append(int(building[i]))
        if buildings[0] == 1:
            buildings[0] = 2
            if length > 1:
                if buildings[1] == 0:
                    buildings[1] = 2
        for i in range(1, length - 1):
            if buildings[i] == 1:
                buildings[i] = 2
                if buildings[i + 1] == 0:
                    buildings[i + 1] = 2
                if buildings[i - 1] == 0:
                    buildings[i - 1] = 2
        if buildings[length - 1] == 1:
            buildings[length - 1] = 2
            if buildings[length - 2] == 0:
                buildings[length - 2] = 2
        print(buildings.count(0))
    else:
        print(0)
    inputs = inputs - 1
