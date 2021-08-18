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
        elem = mapp[road[0]]
        elem[city.index(road[1])] = int(road[2])
        mapp[road[0]] = elem
    itins = eval(input())
    while itins:
        itins -= 1
        route = input().split()
        total = 0
        v = [0] * n
        if route[0] == '1':
            if route[-1] in city:
                print(total)
            else:
                print("ERROR")
        else:
            for r in range(1, len(route)):
                if (route[r] not in city) or v[city.index(route[r])]:
                    total = "ERROR"
                    break
                elif r > 1:
                    if mapp[route[r - 1]][city.index(route[r])]:
                        total += mapp[route[r - 1]][city.index(route[r])]
                    else:
                        total = "ERROR"
                        break
                v[city.index(route[r])] = 1
            print(total)


main()
