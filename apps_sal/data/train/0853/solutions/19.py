try:
    for _ in range(int(input())):
        n = int(input())
        driver = []
        for __ in range(n):
            name = input()
            time = int(input())
            driver.append((name, time))
        driver.sort(key=lambda x: x[1])
        for ele in driver:
            print(ele[0])
except:
    pass
