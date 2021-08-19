def four():
    n = input()
    count = 0
    for i in n:
        if int(i) == 0:
            continue
        elif int(i) == 4:
            count += 1
    print(count)


for _ in range(int(input())):
    four()
