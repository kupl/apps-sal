import sys
sys.setrecursionlimit(10000000)

flag = []


def isSafe(l, x, y, n, m):
    if x >= 0 and x < n and y >= 0 and y < m and l[x][y] == 0:
        return True
    return False


def solveMaze(l, n, m):
    x = solveMazeUtil(l, n, m, 0, 0, 0)
    return x


def solveMazeUtil(l, n, m, x, y, count):

    nonlocal flag

    count += 1
    if x == 0 and y == m - 1:
        if l[x][y] == 0:
            return count
        return -1

    if isSafe(l, x, y, n, m) == True:

        if flag[x][y] == 0:

            flag[x][y] = 1

            # if flag[x-1][y] == 0:
            z = solveMazeUtil(l, n, m, x - 1, y, count)
            if z != -1:
                return z

            # if flag[x][y-1] == 0:
            z = solveMazeUtil(l, n, m, x, y - 1, count)
            if z != -1:
                return z

            # if flag[x][y+1] == 0:
            z = solveMazeUtil(l, n, m, x, y + 1, count)
            if z != -1:
                return z

            # if flag[x+1][y] == 0:
            z = solveMazeUtil(l, n, m, x + 1, y, count)
            if z != -1:
                return z

            return -1

    return -1


def main():

    nonlocal flag
    for q in range(eval(input())):

        a = [int(i) for i in input().split()]
        n = a[0]
        m = a[1]
        l = []

        if a[2] == 0 and a[3] == 0:
            print(-1)

        else:

            flag = [[0 for i in range(m)] for j in range(n)]
            for i in range(n):
                l.append([int(i) for i in input().split()])

            ans = solveMaze(l, n, m)

            if a[2] == 0 or a[3] == 0:
                print(ans)

            else:
                if ans >= 0:
                    print(ans / 2)
                else:
                    print(ans)


main()
