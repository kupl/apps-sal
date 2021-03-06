def main():
    n = eval(input())
    city = input().split()
    m = eval(input())
    mapp = {}
    for c in city:
        mapp[c] = [0] * n
    while m:
        m -= 1
        road = input().split()
        temp = mapp[road[0]]
        temp[city.index(road[1])] = int(road[-1])
        mapp[road[0]] = temp
    t = eval(input())
    while t:
        t -= 1
        dist = 0
        v = [0] * n
        route = input().split()
        if route[0] == '1':
            if route[-1] in city:
                print(dist)
            else:
                print('ERROR')
        else:
            for r in range(1, int(route[0]) + 1):
                if route[r] not in city or v[city.index(route[r])]:
                    dist = 'ERROR'
                    break
                elif r > 1:
                    if mapp[route[r - 1]][city.index(route[r])]:
                        dist += mapp[route[r - 1]][city.index(route[r])]
                    else:
                        dist = 'ERROR'
                        break
                v[city.index(route[r])] = 1
            print(dist)


main()
