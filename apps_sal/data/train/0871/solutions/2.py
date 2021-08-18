import copy


def AllDead(arr):
    var = 1
    for x in arr:
        for y in x:
            if "U" in y or "D" in y or "L" in y or "R" in y:
                var = 0
    return var


def checkMeet(arr):
    ans = 0
    for x in arr:
        for y in x:
            if len(y) >= 2 and '-' not in y:
                ans += (len(y) * (len(y) - 1)) // 2
    return ans


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    lol = [['
    arr = [lol]
    for j in range(n):
        mo = [[x] for x in input()]
        arr += [[['
    arr += [lol]
    meet = 0
    while AllDead(arr) == 0:
        temp = copy.deepcopy(arr)
        for x in range(1, n + 1):
            for y in range(1, m + 1):
                for z in arr[x][y]:
                    if z == 'U':
                        if arr[x - 1][y] == ['
                            do_nothing = 1
                        elif temp[x - 1][y] == ['-']:
                            temp[x - 1][y].remove('-')
                            temp[x - 1][y] += ['U']
                        else:
                            temp[x - 1][y] += ['U']
                        temp[x][y].remove(z)
                        if len(temp[x][y]) == 0:
                            temp[x][y] = ['-']
                    if z == 'D':
                        if arr[x + 1][y] == ['
                            do_nothing = 1
                        elif temp[x + 1][y] == ['-']:
                            temp[x + 1][y].remove('-')
                            temp[x + 1][y] += ['D']
                        else:
                            temp[x + 1][y] += ['D']
                        temp[x][y].remove(z)
                        if len(temp[x][y]) == 0:
                            temp[x][y] = ['-']
                    if z == 'L':
                        if arr[x][y - 1] == ['
                            do_nothing = 1
                        elif temp[x][y - 1] == ['-']:
                            temp[x][y - 1].remove('-')
                            temp[x][y - 1] += ['L']
                        else:
                            temp[x][y - 1] += ['L']
                        temp[x][y].remove(z)
                        if len(temp[x][y]) == 0:
                            temp[x][y] = ['-']
                    if z == 'R':
                        if arr[x][y + 1] == ['
                            do_nothing = 1
                        elif temp[x][y + 1] == ['-']:
                            temp[x][y + 1].remove('-')
                            temp[x][y + 1] += ['R']
                        else:
                            temp[x][y + 1] += ['R']
                        temp[x][y].remove(z)
                        if len(temp[x][y]) == 0:
                            temp[x][y] = ['-']
        arr = copy.deepcopy(temp)
        meet += checkMeet(arr)
    print(meet)
