def main():
    T = int(input())
    for test in range(T):
        N = int(input())
        buildingList = input().strip()
        totalStanding = N
        for (index, building) in enumerate(buildingList):
            if building == '1' or (index > 0 and buildingList[index - 1] == '1') or (index < N - 1 and buildingList[index + 1] == '1'):
                totalStanding -= 1
        print(totalStanding)


def __starting_point():
    main()


__starting_point()
