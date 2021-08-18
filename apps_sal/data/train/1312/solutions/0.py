import sys

spoon = ["SPOON", "spoon"]


def main():
    try:
        tc = int(input())
        while tc > 0:
            tc = tc - 1
            [r, c] = input().split()
            r = int(r)
            c = int(c)
            k = 0
            flag = 0
            matrix = [0] * r
            i = 0
            while i < r:
                matrix[i] = input()
                i = i + 1

            for m in matrix:
                for s in m:
                    if s == spoon[0][k] or s == spoon[1][k]:
                        k = k + 1
                        if k == 5:
                            flag = 1
                            k = 0
                            break
                    else:
                        k = 0

            if flag == 1:
                print("There is a spoon!")
                continue

            i = 0
            k = 0
            while i < c:
                j = 0
                while j < r:
                    if matrix[j][i] == spoon[0][k] or matrix[j][i] == spoon[1][k]:
                        k = k + 1
                        if k == 5:
                            flag = 1
                            k = 0
                            break
                    else:
                        k = 0
                    j = j + 1
                i = i + 1

            if flag == 1:
                print("There is a spoon!")
                continue

            print("There is indeed no spoon!")

    except:
        return 0


main()
