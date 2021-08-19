# cook your dish here
T = int(input())

for i in range(T):
    N, data, D, People = int(input()), list(map(int, list(input()))), int(input()), list(map(int, input().split()))

    data.insert(0, "|"), data.append("|")
    infected = []
    for i in range(1, N + 1):
        if(data[i] == 1):
            infected.append(i)

    i = 0
    while(i < D):
        boundary = People[i] + i
        data.insert(boundary, "|")
        times = len(infected)
        for p in range(times):
            index = infected[p]
            if(index >= boundary):
                index += 1
                infected[p] += 1
            if(data[index] == 1):
                if(data[index + 1] == 0):
                    data[index + 1] = 1
                    infected.append(index + 1)
                if(data[index - 1] == 0):
                    data[index - 1] = 1
                    infected.append(index - 1)
            else:
                infected.remove(index)
                times -= 1
        i += 1
        infected.sort()

    print(data.count(1))
