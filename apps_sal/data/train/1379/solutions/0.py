import sys
import math


def main(filename):
    inputfile = open(filename, 'rU')
    data = inputfile.readlines()
    T = data.pop(0)
    ans = []
    ansstring = str()
    explored = []
    for i in T:
        if i in explored:
            # print explored
            for j in range(len(ans)):
                if ans[j][0] == i:
                    ans[j][1] += 1
        else:
            ans.append([i, 1])
            explored.append(i)
    for i in ans:
        ansstring += i[0] + str(i[1])
    print(ansstring)

    inputfile.close()


def __starting_point():
    main(sys.argv[1])


__starting_point()
