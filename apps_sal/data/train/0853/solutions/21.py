def takeSecond(elem):
    return elem[1]


t = int(input())
for _ in range(t):
    n = int(input())
    drivers_and_time = []
    for _ in range(n):
        driver = input()
        his_time = int(input())
        drivers_and_time.append((driver, his_time))
    drivers_and_time.sort(key=takeSecond)
    for item in drivers_and_time:
        print(item[0])
