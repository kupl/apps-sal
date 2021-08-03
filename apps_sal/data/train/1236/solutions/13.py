testcase = int(input())
while testcase:
    l = int(input())
    data = input()
    count = 0
    for i in range(l - 1):
        if data[i] == data[i + 1]:
            count += 1
    print(count)
    testcase -= 1
