tulu = int(input())
for _ in range(tulu):
    n = int(input())
    string = input()
    flag = False
    counter = 0
    frequency = 1
    for i in string:
        if i == '0' and flag == False:
            flag = True
            continue
        if flag and i == '0':
            frequency += 1
        if flag and i == '1':
            counter += frequency
    flag = False
    frequency = 1
    for i in string:
        if i == '1' and flag == False:
            flag = True
            continue
        if flag and i == '1':
            frequency += 1
        if flag and i == '0':
            counter += frequency
    print(counter)
